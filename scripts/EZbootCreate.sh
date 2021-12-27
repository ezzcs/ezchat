sudo qemu-system-x86_64 -name Lhasa -m 8192 -smp 2 -cpu host -hda /mnt/sda5/ezzcs/qemu/data/ezBoot.qcow2 -cdrom /mnt/sda5/ezzcs/qemu/linux/ubuntu-20.04-desktop-amd64.iso -boot c -enable-kvm 

