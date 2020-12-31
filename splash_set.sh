#!/bin/bash

sudo echo 'disable_splash=1' >> /boot/config.txt
sudo sed -i 's/^message_sprite/#&/' /usr/share/plymouth/themes/pix/pix.script
sudo sed -i 's/^Plymouth.SetUpdate/#&/' /usr/share/plymouth/themes/pix/pix.script
sudo sed -i 's/console=tty1/console=tty3/' /boot/cmdline.txt


if grep -q splash /boot/cmdline.txt
then
	echo ' '
else
	echo 'splash' >> /boot/cmdline.txt
fi

if grep -q quiet /boot/cmdline.txt
then
	echo ' '
else
	echo 'quiet' >> /boot/cmdline.txt
fi

if grep -q plymouth.ignore-serial-consoles /boot/cmdline.txt
then
	echo ' '
else
	echo 'plymouth.ignore-serial-consoles' >> /boot/cmdline.txt
fi

if grep -q logo.nologo /boot/cmdline.txt
then
	echo ' '
else
	echo 'logo.nologo' >> /boot/cmdline.txt
fi

if grep -q vt.global_cursor_default=0 /boot/cmdline.txt
then
	echo ' '
else
	echo 'vt.global_cursor_default=0' >> /boot/cmdline.txt
fi
