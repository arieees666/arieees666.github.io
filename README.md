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
 - Sept 23, 2020: `Reversed lab6B, found continuous memory read in hash_pass - can overwrite attempts,results variables. Haven't found a way to exploit it yet. Read some self improvement articles from azerialabs to have motivation/to learn a better learning process`
 - Sept 24, 2020: `Skipped lab6B, stack isn't the same witht the writeups I read i dunno why. It doesn't let me leak the return address, only until the attempts and results variable. Worked on lab6A instead, where I identified the vuln quickly and got it to segfault. Was able to redirect code flow by partial overwrite but no plan from that point. Also started learning how to use git, made my first commit through command line today.`
 - Sept 25, 2020: `Another productive day, solved a lot of challenges from EKOPARTY, then some from darkCTF. Will continue playing as there are 11 ctfs this weekend`
 - Sept 26-27, 2020: `Got pretty busy with ctfs, 11 ctfs in 2 days. Focused mostly on EKOPARTY which I placed 92nd and some Bsides Boston`
 - Sept 28, 2020: `Created writeups for solved challenges, tried to solve DarkCTF pwnables which I haven't got the chance to solve`
 - Sept 29, 2020: `Started learning about SIGROP`
 - Sept 30, 2020: `Understood how to bypass aslr. Created a discord bot to assign a role when a certain emoji is reacted`

## October
 - Oct 1, 2020: `Started learning about heap exploitation, solved my first uaf :)`
 - Oct 2, 2020: `Played around and solved lab7C, but still need to understand heap memory deeper`
 - Oct 3-4, 2020: `Joined in the b01lers bootcamp CTF to test what I learned about memory corruption the past month; satisfied with the results, placed 92nd/500+ teams`
 - Oct 5, 2020: `Created writeups for solved challenges.`
 - Oct 6-7, 2020: `Started reading on heap internals`
 - Oct 8, 2020: `Not much, focused on finishing schoolworks. Reread heap internal articles`
 - Oct 9, 2020: `Solved the stack canary chall from b01lers. Continued reading on heap internals, beginning to understand something somehow`
 - Oct 10-11, 2020: `Focused on playing DamCTF, though I only solved the easy ones.`
 - Oct 12, 2020: `Currently experimenting on what bin freed chunks go to. Results differ from articles I have read, which confuses me. Will read some more and continue tomorrow.`
 - Oct 13, 2020: `I think I finally understand which bins chunks go when they are freed. I'll read some more then start learning how to actually do exploits.`
 - Oct 14, 2020: `Realized some of the articles I read aren't applicable since the glibc version on my device is the one with tcache implemented; so instead of going to their respective bins immediately, chunks are being placed into the tcache bin. Found out after debugging a fastbin technique.`
 - Oct 15-16, 2020: `Got pretty busy with schoolworks didn't have time to learn pwn :(((`
 - Oct 17, 2020: `Focusing on hacktober ctf. Attempted to play the pwn challenge from N1CTF with had the highest amount of solves, it was a heap challenge which I managed to segfault using UAF, but still figuring out the next step/s.`
 - Oct 18, 2020: `Disappointed and feel I wasted my time on hacktober ctf (challs were very guessy asf). Will continue learning heap later tonight.`
 - Oct 19, 2020: `Began installing the needed tools to debug heap challs (pwninit, rust)`
 - Oct 20, 2020: `Successfully installed the needed tools and dependencies, time to start learning heap hacking.`
 - Oct 21, 2020: `Played some syskronCTF challs`
 - Oct 22, 2020: `Figured out how to debug with ld_preload and with the right ld patched into the binary`
 - Oct 23-31, 2020: `Participated in quite a lot of ctfs that happened during this time period. Details to come later.`

## November
 - Nov 1, 2020: `Played in CyberyoddhaCTF and NACTF, solved a lot of challs which are pretty good as an indicator of my current knowledge`
 - Nov 2, 2020: `Solved four android reversing challs from MOBISEC`
 - Nov 3, 2020: `Took a step back in order to reorganize my thoughts`
 - Nov 4-5, 2020: `Attempted to try cttt again but failed. Created writeups for solved NACTF tasks`
 - Nov 6, 2020: `Did a run down of the writeups for the heap challenges from NACTF posted by other people, will begin analysis tomorrow. Started watching heap lecture from pwncollege`
 - Nov 7-8, 2020: `Participated and solved challenges in Sunshine CTF instead of learning heap and doing schoolwork`
 - Nov 9, 2020: `Beginning to have an understanding of the tcache poison technique after reading writeups of NACTF's covid tracker challenge. Writeup to come later.`
 - Nov 10, 2020: `Was able to pop a shell after following HK's writeup. Still have questions regarding on how editing/controlling the fd pointer affects the exploit and how to piece it all together. Might need to reread malloc internals again.`
 - Nov 11-12, 2020: `Continuing analysis for the tcache poison exploit after doing midterms requirements. Still getting clarification on how the exploit works. Learned about __free/__malloc hooks.`
 - Nov 13, 2020: `I FINALLY UNDERSTOOD WHAT'S HAPPENING WITH THE EXPLOIT. EVEN CHANGED THE ORIGINAL CODE TO MAKE IT MUCH BETTER`