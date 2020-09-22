## About me
#### I'm just a student deeply interested in cybersec, especially on the fields of binary exploitation, exploit development, and anything malware related. If I get versed with pwn and reversing, I will apply what I've learned to conduct research regarding exploitation on the Android platform. Still getting started on the field tho, but will fearlessly continue to learn and grow. Aiming to be one of the top tier hackers within and representing the Philippines. *About will be updated sooner or later*

### Progress Logs
#### Since I stopped playing ctfs for a year (laptop broke rip) and only as of mid August that I got a new hand-me-down old model chromebook, I wanted to start learning exploit development seriously this time (even with school kinda being annoying). Thus, I began to set a goal that I do something exploit dev/pwning related everyday and make sure to document what I did. 
 - Sept 01, 2020: `Successfully finished memory corruption labs`
 - Sept 02, 2020: `Finished basic bof + shellcode challenge, stuck at shellcode lab2B`
 - Sept 03, 2020: `Finally wrote working open,read,write shellcode. Process = write shellcode, debug, rewrite shellcode`
 - Sept 04, 2020: `Failed to do something, sorry self`
 - Sept 05, 2020: `Done with shellcode lab :) learned how to create custom shellcode, but still needs improvement`
 - Sept 06, 2020: `Finished format string lecture problems, learned how to do multiple writes with format string vulns, got shell in fmt_lec04. Now have a better understanding on fmt str exploits.`
 - Sept 07, 2020: `Solved lab4C (read strings from stack using fmtstr exploit); partial solve for lab4B`
 - Sept 08, 2020: `Solved lab4B, but not satisfied. Find a way to execute exploit outside gdb`
 - Sept 09, 2020: `found and triggered vulnerability on lab4A, got stuck with figuring out how many bytes are written, came up with an exploit plan but failed to do so. Peeked at a writeup and saw similar plan (maybe consider this a partial solve?)`
 - Sept 10, 2020: `Played around with rop lecture binaries, couldn't do anything because of canaries`
 - Sept 11, 2020: `Got shell with lab5C, simple ret2libc. Partial solve for lab5B (was able to execute /bin/dash but sigabrts prematurely)`
 - Sept 12, 2020: `Productive day, solved baby pwn from csaw quals + 1st python sandbox escape, baby rev from flareon`
 - Sept 13, 2020: `Reverse engineered prehistoric mario chall from ALLESCTF, wrote a bruteforce script for correct box values. Will begin writeups for solved CSAW quals challenges`
 - Sept 14, 2020: `Began initial analysis of RPISEC project 1 binary, tw33tchainz`
 - Sept 15, 2020: `Was able to reverse engineer the custom hash function in order to retrieve secret pass to verify as admin. Enabled debug mode and triggered format string vulnerability in print_menu()`
 - Sept 16, 2020: `Restructured code to connect gdb with running process. Also fixed code to set debug mode on for the challenge. Found a way to hijack control flow. Changed exit@got address to 0x1337 as a test, then entered exit functionality resulted in segfault invalid address 0x1337 :)`
 - Sept 17, 2020: `Popped a shell for project1 :) Format string multiple writes to overwrite exit got to stack then execute shellcode from there. Fucking satisfying.`
 - Sept 18, 2020: `Rootcon CTF quals started, focused on pwn chall only, but got stuck.`
 - Sept 19, 2020: `Continued attempt on previous work but to no avail. Get a glimpse of how hard rootcon ctf is and promise to self to come back stronger for next year. Aside from that, solved three challs (2 pwn/1 rev) from downunder ctf. Continuing to work on chall #3`
 - Sept 20, 2020: `Solved return to revenge chall from DownUnder ctf, learned to bypass baby seccomp`
 - Sept 21, 2020: `Published writeups for solved downunder ctf challenges. Analyzed exploit for revenge chall and echo server`
 - Sept 22, 2020: `Found and triggered vulnerabilities for lab6C. Had to peek at a writeup to know that I needed a partial overwrite to solve the chall (I overcomplicated reversing it and trying to think of the solution when in fact it was that simple)`
