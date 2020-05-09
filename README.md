# What ?

For me libvirt is far too much bloated, I also want to manage network myself not with virsh. I use qemu a lot and like it's simplicity. Since qemu commands can be very long, and didn't know how to manage my vm in a sane, tided, and declarative way. I did this tiny kiss vm manager (which also can launch anything).

# How to ?

make a ~/.config/qissmu.py with this python code :

```    
vm = dict()

vm["gentoo"] = """
qemu-system-x86_64 \
    -enable-kvm \
    -smp 12 \
    -m 8192 \
    -nic user,hostfwd=tcp::10022-:22,model=virtio \
    -drive file=/mnt/nas/VM/gentoo.img,media=disk,if=virtio \
    -sdl
"""

vm["demo"] = """
qemu-system-x86_64 \
    -enable-kvm \
    -m 2048 \
    -nic user,model=virtio \
    -drive file=alpine.qcow2,media=disk,if=virtio \
    -cdrom alpine-standard-3.8.0-x86_64.iso \
    -sdl
"""

vm["demo2"] = """
qemu-system-x86_64 \
    -sdl
"""
```
## When you get amnesia :
    
    qissmu list

## When you want to launch a vm
    
    qissmu start demo

It's simple, it's kiss.

# I want to translate my qemu cmd to a service ?

https://wiki.archlinux.org/index.php/QEMU#With_systemd_service
