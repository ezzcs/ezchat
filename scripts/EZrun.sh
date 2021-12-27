sudo qemu-system-x86_64 -name Lhasa -m 8192 -smp 2 -cpu host -hda /mnt/sda5/ezzcs/qemu/data/ezBoot.qcow2  -boot c -enable-kvm -net nic -net user,hostfwd=tcp::5555-:22,hostfwd=tcp::80-:80,hostfwd=tcp::8001-:8001,

