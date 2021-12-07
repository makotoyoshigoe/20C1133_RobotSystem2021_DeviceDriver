//SPDX-License-Identifer: GPL-3.0
//Copyright (c) 2021 Makoto Yoshigoe & Ryuichi Ueda. All rights reserved

#include <linux/module.h>
#include <linux/fs.h>
#include <linux/cdev.h>
#include <linux/device.h>
#include <linux/uaccess.h>
#include <linux/io.h>
#include <linux/delay.h>

MODULE_AUTHOR("MakotoYoshigoe, RyuichiUeda");
MODULE_DESCRIPTION("driver for LED control");
MODULE_LICENSE("GPL");
MODULE_VERSION("0.0.1");
#define PIN 17
#define ON 7
#define OFF 10

static dev_t dev;
static struct cdev cdv;
static struct class *cls = NULL;
static volatile u32 *gpio_base = NULL;
int pin[PIN] = {21, 20, 26, 16, 19, 13, 12, 6, 5, 25, 24, 23, 22, 27, 18, 17, 4};
static ssize_t calculator(struct file* filp, const char* buf, size_t count, loff_t* pos){
	char c;
	int i = 0, j = 0;
	static int cnt = 0;
	if(copy_from_user(&c, buf, sizeof(c))) return -EFAULT;
	if(c == 'e'){
		for(i = 0; i < 4; i++){
			for(j = 0; j < PIN; j++) gpio_base[ON] = 1 << pin[j];
			msleep(250);
			for(j = 0; j < PIN; j++) gpio_base[OFF] = 1 << pin[j];
			msleep(250);
		}
	}else if(c == 'w'){
		for(i = 0; i < PIN; i++){
			for(j = 0; j < PIN; j++){
				if(j == i) gpio_base[ON] = 1 << pin[j];
				else gpio_base[OFF] = 1 << pin[j];
			}	
			msleep(100);
		}
		for(i = PIN; i >= -1; i--){
			for(j = PIN; j >= -1; j--){
				if(j == i) gpio_base[ON] = 1 << pin[j];
				else gpio_base[OFF] = 1 << pin[j];
			}
			msleep(100);
		}
	}else{
		if(c == '1'|| c == '2') gpio_base[ON] = 1 << pin[cnt%PIN];
		else gpio_base[OFF] = 1 << pin[cnt%PIN];
		cnt++;
	}
	return 1;
}
static struct file_operations led_fops = {
	.owner = THIS_MODULE,
	.write = calculator,
};

static int __init init_mod(void){
	int retval, i = 0;
	gpio_base = ioremap_nocache(0xfe200000, 0xA0);
	for(i = 0; i < PIN; i++){
		const u32 led = pin[i]; //GPIOの番号
	        const u32 index = led/10; //列
		const u32 shift = (led%10)*3;//行
		const u32 mask = ~(0x7 << shift);
		gpio_base[index] = (gpio_base[index] & mask) | (0x1 << shift);
	}
	retval = alloc_chrdev_region(&dev, 0, 1, "calculator");
	if(retval < 0){
		printk(KERN_ERR "alloc_chrdev_region failed.\n");
		return retval;
	}
	printk(KERN_INFO "%s is loaded. major:%d\n", __FILE__, MAJOR(dev));
	
	cdev_init(&cdv, &led_fops);
	retval = cdev_add(&cdv, dev, 1);
	if(retval < 0){
		printk(KERN_ERR "cdev_add failed. major:%d, minor:%d\n", MAJOR(dev), MINOR(dev));
		return retval;
	}
	cls = class_create(THIS_MODULE, "calculator");
	if(IS_ERR(cls)){
		printk(KERN_ERR "class_create failed.");
		return PTR_ERR(cls);
	}
	device_create(cls, NULL, dev, NULL, "calculator%d", MINOR(dev));
	printk(KERN_INFO"end\n");
	return 0;
}

static void __exit cleanup_mod(void){
	cdev_del(&cdv);
	device_destroy(cls, dev);
	class_destroy(cls);
	unregister_chrdev_region(dev, 1); 
	printk(KERN_INFO "%s is unloaded. major:%d\n", __FILE__, MAJOR(dev));
	printk(KERN_INFO"end1\n");
}

module_init(init_mod);
module_exit(cleanup_mod);
