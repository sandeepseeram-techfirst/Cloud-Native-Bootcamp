### strace 
strace is a powerful diagnostic, debugging, and troubleshooting tool for Linux systems. It is primarily used to trace system calls and signals received by a process. This can be incredibly useful for debugging software, understanding program behavior, and identifying performance bottlenecks.

###### controlplane:~$ strace ls 
execve("/usr/bin/ls", ["ls"], 0x7ffefc059650 /* 17 vars */) = 0
brk(NULL)                               = 0x5e35e3527000
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x6ffe066d3000
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=65971, ...}) = 0
mmap(NULL, 65971, PROT_READ, MAP_PRIVATE, 3, 0) = 0x6ffe066c2000
close(3)                                = 0
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libselinux.so.1", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\0\0\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0644, st_size=174472, ...}) = 0
mmap(NULL, 181960, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x6ffe06695000
mmap(0x6ffe0669b000, 118784, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x6000) = 0x6ffe0669b000
mmap(0x6ffe066b8000, 24576, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x23000) = 0x6ffe066b8000
mmap(0x6ffe066be000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x29000) = 0x6ffe066be000
mmap(0x6ffe066c0000, 5832, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x6ffe066c0000
close(3)                                = 0
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\220\243\2\0\0\0\0\0"..., 832) = 832
pread64(3, "\6\0\0\0\4\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0"..., 784, 64) = 784
fstat(3, {st_mode=S_IFREG|0755, st_size=2125328, ...}) = 0
pread64(3, "\6\0\0\0\4\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0"..., 784, 64) = 784
mmap(NULL, 2170256, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x6ffe06400000
mmap(0x6ffe06428000, 1605632, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x28000) = 0x6ffe06428000
mmap(0x6ffe065b0000, 323584, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1b0000) = 0x6ffe065b0000
mmap(0x6ffe065ff000, 24576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1fe000) = 0x6ffe065ff000
mmap(0x6ffe06605000, 52624, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x6ffe06605000
close(3)                                = 0
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libpcre2-8.so.0", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\0\0\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0644, st_size=625344, ...}) = 0
mmap(NULL, 627472, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x6ffe06366000
mmap(0x6ffe06368000, 450560, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x2000) = 0x6ffe06368000
mmap(0x6ffe063d6000, 163840, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x70000) = 0x6ffe063d6000
mmap(0x6ffe063fe000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x97000) = 0x6ffe063fe000
close(3)                                = 0
mmap(NULL, 12288, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x6ffe06692000
arch_prctl(ARCH_SET_FS, 0x6ffe06692800) = 0
set_tid_address(0x6ffe06692ad0)         = 10322
set_robust_list(0x6ffe06692ae0, 24)     = 0
rseq(0x6ffe06693120, 0x20, 0, 0x53053053) = 0
mprotect(0x6ffe065ff000, 16384, PROT_READ) = 0
mprotect(0x6ffe063fe000, 4096, PROT_READ) = 0
mprotect(0x6ffe066be000, 4096, PROT_READ) = 0
mprotect(0x5e35df66e000, 8192, PROT_READ) = 0
mprotect(0x6ffe0670b000, 8192, PROT_READ) = 0
prlimit64(0, RLIMIT_STACK, NULL, {rlim_cur=8192*1024, rlim_max=RLIM64_INFINITY}) = 0
munmap(0x6ffe066c2000, 65971)           = 0
statfs("/sys/fs/selinux", 0x7fffb9f6f190) = -1 ENOENT (No such file or directory)
statfs("/selinux", 0x7fffb9f6f190)      = -1 ENOENT (No such file or directory)
getrandom("\xe8\x68\xe4\xec\x41\xef\xc8\xec", 8, GRND_NONBLOCK) = 8
brk(NULL)                               = 0x5e35e3527000
brk(0x5e35e3548000)                     = 0x5e35e3548000
openat(AT_FDCWD, "/proc/filesystems", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0444, st_size=0, ...}) = 0
read(3, "nodev\tsysfs\nnodev\ttmpfs\nnodev\tbd"..., 1024) = 414
read(3, "", 1024)                       = 0
close(3)                                = 0
access("/etc/selinux/config", F_OK)     = -1 ENOENT (No such file or directory)
ioctl(1, TCGETS, {c_iflag=ICRNL|IXON, c_oflag=NL0|CR0|TAB0|BS0|VT0|FF0|OPOST|ONLCR, c_cflag=B38400|CS8|CREAD, c_lflag=ISIG|ICANON|ECHO|ECHOE|ECHOK|IEXTEN|ECHOCTL|ECHOKE, ...}) = 0
ioctl(1, TIOCGWINSZ, {ws_row=35, ws_col=141, ws_xpixel=0, ws_ypixel=0}) = 0
openat(AT_FDCWD, ".", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 3
fstat(3, {st_mode=S_IFDIR|0700, st_size=4096, ...}) = 0
getdents64(3, 0x5e35e352cc40 /* 21 entries */, 32768) = 656
getdents64(3, 0x5e35e352cc40 /* 0 entries */, 32768) = 0
close(3)                                = 0
fstat(1, {st_mode=S_IFCHR|0620, st_rdev=makedev(0x88, 0), ...}) = 0
write(1, "filesystem\n", 11filesystem
)            = 11
close(1)                                = 0
close(2)                                = 0
exit_group(0)                           = ?
+++ exited with 0 +++
controlplane:~$ 


First we find the Apiserver process


ps aux | grep kube-apiserver

Then we use strace and pass the PID


strace -p 19890 -f # use your PID

# we use -f for "follow forks"

Well, that's a bit much. Let's count and summarise


strace -p 19890 -f -cw # use your PID

# run for a bit, then abort with Ctrl+C
# we should see a nice list of all syscalls.