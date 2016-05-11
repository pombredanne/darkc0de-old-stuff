# Linux kernel syscall list from Linux 2.6.21 for i386
#
# List extracted from Linux kernel source code, see:
#    arch/i386/kernel/syscall_table.S
SYSCALL_NAMES = {
      0: "restart_syscall",
      1: "exit",
      2: "fork",
      3: "read",
      4: "write",
      5: "open",
      6: "close",
      7: "waitpid",
      8: "creat",
      9: "link",
     10: "unlink",
     11: "execve",
     12: "chdir",
     13: "time",
     14: "mknod",
     15: "chmod",
     16: "lchown16",
#    17: -
     18: "stat",
     19: "lseek",
     20: "getpid",
     21: "mount",
     22: "oldumount",
     23: "setuid16",
     24: "getuid16",
     25: "stime",
     26: "ptrace",
     27: "alarm",
     28: "fstat",
     29: "pause",
     30: "utime",
#    31: -
#    32: -
     33: "access",
     34: "nice",
#    35: -
     36: "sync",
     37: "kill",
     38: "rename",
     39: "mkdir",
     40: "rmdir",
     41: "dup",
     42: "pipe",
     43: "times",
#    44: -
     45: "brk",
     46: "setgid16",
     47: "getgid16",
     48: "signal",
     49: "geteuid16",
     50: "getegid16",
     51: "acct",
     52: "umount",
#    53: -
     54: "ioctl",
     55: "fcntl",
#    56: -
     57: "setpgid",
#    58: -
     59: "oldolduname",
     60: "umask",
     61: "chroot",
     62: "ustat",
     63: "dup2",
     64: "getppid",
     65: "getpgrp",
     66: "setsid",
     67: "sigaction",
     68: "sgetmask",
     69: "ssetmask",
     70: "setreuid16",
     71: "setregid16",
     72: "sigsuspend",
     73: "sigpending",
     74: "sethostname",
     75: "setrlimit",
     76: "old_getrlimit",
     77: "getrusage",
     78: "gettimeofday",
     79: "settimeofday",
     80: "getgroups16",
     81: "setgroups16",
     82: "old_select",
     83: "symlink",
     84: "lstat",
     85: "readlink",
     86: "uselib",
     87: "swapon",
     88: "reboot",
     89: "old_readdir",
     90: "old_mmap",
     91: "munmap",
     92: "truncate",
     93: "ftruncate",
     94: "fchmod",
     95: "fchown16",
     96: "getpriority",
     97: "setpriority",
#    98: -
     99: "statfs",
    100: "fstatfs",
    101: "ioperm",
    102: "socketcall",
    103: "syslog",
    104: "setitimer",
    105: "getitimer",
    106: "newstat",
    107: "newlstat",
    108: "newfstat",
    109: "olduname",
    110: "iopl",
    111: "vhangup",
#   112: old "idle"
    113: "vm86old",
    114: "wait4",
    115: "swapoff",
    116: "sysinfo",
    117: "ipc",
    118: "fsync",
    119: "sigreturn",
    120: "clone",
    121: "setdomainname",
    122: "uname",
    123: "modify_ldt",
    124: "adjtimex",
    125: "mprotect",
    126: "sigprocmask",
#   127: old "create_module"
    128: "init_module",
    129: "delete_module",
#   130: old "get_kernel_syms"
    131: "quotactl",
    132: "getpgid",
    133: "fchdir",
    134: "bdflush",
    135: "sysfs",
    136: "personality",
#   137: reserved for afs_syscall
    138: "setfsuid16",
    139: "setfsgid16",
    140: "llseek",
    141: "getdents",
    142: "select",
    143: "flock",
    144: "msync",
    145: "readv",
    146: "writev",
    147: "getsid",
    148: "fdatasync",
    149: "sysctl",
    150: "mlock",
    151: "munlock",
    152: "mlockall",
    153: "munlockall",
    154: "sched_setparam",
    155: "sched_getparam",
    156: "sched_setscheduler",
    157: "sched_getscheduler",
    158: "sched_yield",
    159: "sched_get_priority_max",
    160: "sched_get_priority_min",
    161: "sched_rr_get_interval",
    162: "nanosleep",
    163: "mremap",
    164: "setresuid16",
    165: "getresuid16",
    166: "vm86",
#   167: old "query_module"
    168: "poll",
    169: "nfsservctl",
    170: "setresgid16",
    171: "getresgid16",
    172: "prctl",
    173: "rt_sigreturn",
    174: "rt_sigaction",
    175: "rt_sigprocmask",
    176: "rt_sigpending",
    177: "rt_sigtimedwait",
    178: "rt_sigqueueinfo",
    179: "rt_sigsuspend",
    180: "pread64",
    181: "pwrite64",
    182: "chown16",
    183: "getcwd",
    184: "capget",
    185: "capset",
    186: "sigaltstack",
    187: "sendfile",
#   188: (reserved)
#   189: (reserved)
    190: "vfork",
    191: "getrlimit",
    192: "mmap2",
    193: "truncate64",
    194: "ftruncate64",
    195: "stat64",
    196: "lstat64",
    197: "fstat64",
    198: "lchown",
    199: "getuid",
    200: "getgid",
    201: "geteuid",
    202: "getegid",
    203: "setreuid",
    204: "setregid",
    205: "getgroups",
    206: "setgroups",
    207: "fchown",
    208: "setresuid",
    209: "getresuid",
    210: "setresgid",
    211: "getresgid",
    212: "chown",
    213: "setuid",
    214: "setgid",
    215: "setfsuid",
    216: "setfsgid",
# -------------------------------
    217: "pivot_root",
    218: "mincore",
    219: "madvise",
    220: "getdents64",
    221: "fcntl64",
#   222: -
#   223: -
    224: "gettid",
    225: "readahead",
    226: "setxattr",
    227: "lsetxattr",
    228: "fsetxattr",
    229: "getxattr",
    230: "lgetxattr",
    231: "fgetxattr",
    232: "listxattr",
    233: "llistxattr",
    234: "flistxattr",
    235: "removexattr",
    236: "lremovexattr",
    237: "fremovexattr",
    238: "tkill",
    239: "sendfile64",
    240: "futex",
    241: "sched_setaffinity",
    242: "sched_getaffinity",
    243: "set_thread_area",
    244: "get_thread_area",
    245: "io_setup",
    246: "io_destroy",
    247: "io_getevents",
    248: "io_submit",
    249: "io_cancel",
    250: "fadvise64",
#   251: -
    252: "exit_group",
    253: "lookup_dcookie",
    254: "epoll_create",
    255: "epoll_ctl",
    256: "epoll_wait",
    257: "remap_file_pages",
    258: "set_tid_address",
    259: "timer_create",
    260: "timer_settime",
    261: "timer_gettime",
    262: "timer_getoverrun",
    263: "timer_delete",
    264: "clock_settime",
    265: "clock_gettime",
    266: "clock_getres",
    267: "clock_nanosleep",
    268: "statfs64",
    269: "fstatfs64",
    270: "tgkill",
    271: "utimes",
    272: "fadvise64_64",
#   273: -
    274: "mbind",
    275: "get_mempolicy",
    276: "set_mempolicy",
    277: "mq_open",
    278: "mq_unlink",
    279: "mq_timedsend",
    280: "mq_timedreceive",
    281: "mq_notify",
    282: "mq_getsetattr",
    283: "kexec_load",
    284: "waitid",
#   285: -
    286: "add_key",
    287: "request_key",
    288: "keyctl",
    289: "ioprio_set",
    290: "ioprio_get",
    291: "inotify_init",
    292: "inotify_add_watch",
    293: "inotify_rm_watch",
    294: "migrate_pages",
    295: "openat",
    296: "mkdirat",
    297: "mknodat",
    298: "fchownat",
    299: "futimesat",
    300: "fstatat64",
    301: "unlinkat",
    302: "renameat",
    303: "linkat",
    304: "symlinkat",
    305: "readlinkat",
    306: "fchmodat",
    307: "faccessat",
    308: "pselect6",
    309: "ppoll",
    310: "unshare",
    311: "set_robust_list",
    312: "get_robust_list",
    313: "splice",
    314: "sync_file_range",
    315: "tee",
    316: "vmsplice",
    317: "move_pages",
    318: "getcpu",
    319: "epoll_pwait",
}

