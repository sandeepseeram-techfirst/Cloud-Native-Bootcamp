
# Introduction to Distributed File Systems
Distributed file systems extend the abstractions of local file systems and are one of the primary building blocks of any distributed service.


### Local File System	 
FAT32 - Legacy file system, compatible across OSs, but supports only files < 4GB
NTFS	Used by Windows; supports large files, permissions, encryption
ext3/ext4	Common in Linux systems; journaling (ext4 adds better performance and larger volumes)
APFS	Apple File System; used in macOS for better speed and encryption
XFS	High-performance journaling file system used in enterprise Linux systems

## The Google File System (GFS)
