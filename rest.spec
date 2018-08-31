About source code and creating software, which are a necessary background for an RPM Packager.

1.source code:
    by bash
    by python
    by C
source code becomes machine code-instructions:
    1.1.the program is natively compiled.
        Natively compiled software is software written in a programming language that compiles to machine code, 
        with a resulting binary executable file. Such software can be run stand-alone.
        
        RPM packages built this way are architecture -specific. 
        This means that if you compile such software on a computer that uses a 64-bit (x86_64) AMD or Intel processor, 
        it will not execute on a 32-bit (x86) AMD or Intel processor. 
        The resulting package will have architecture specified in its name.
        
        program ->  machine code(can be run or executed)    ->  execute
        
        C language
        Manual Building
        cello.c
        #include <stdio.h>
        int main(void) {
            printf("Hello World\n");
            return 0;
        }
        gcc -g -o cello cello.c
        ./cello
        
        Automated Building
        Makefile(same directory as cello.c)
        cello:
                gcc -g -o cello cello.c
        clean:
                rm cello
        run make/make clean
        
    1.2.Interpreted Code
        Some programming languages, such as bash or Python, do not compile to machine code. 
        Instead, their programs' source code is executed step by step, without prior transformations, 
        by a Language Interpreter or a Language Virtual Machine.

        Software written entirely in interpreted programming languages is not architecture -specific. 
        Hence, the resulting RPM Package will have string noarch in its name.

        Interpreted languages are either byte-compiled or raw-interpreted. 
        These two types differ in program build process and in packaging procedure.
        1.2.1.the program is interpreted by raw interpreting.
            Raw-interpreted language programs do not need to be compiled at all, they are directly executed by the interpreter.
            
            execute directly
            bello
            #!/bin/bash
            printf "hello world\n"
            
            ./bello
                                    
        1.2.2.the program is interpreted by byte compiling.
            Byte-compiled languages need to be compiled into byte code, which is then executed by the language virtual machine.
            
            program ->  byte code   -> execute by the language virtual machine
            
            Python source code can also be raw-interpreted, but the byte-compiled version is faster.
            pello.py    ->  byte code(is executed by the python language virtual machine)
            pello.py
            #!/usr/bin/env python
            # -*- coding:utf-8 -*-
            print("Hello world")
            
            python -m compileall pello.py
            python pello.cpython-36.pyc

2.Patching software
A patch is source code that updates other source code.
    step1:
        cello.c
        #include <stdio.h>
        int main(void) {
            printf("Hello World\n");
            return 0;
        }
    step2:
        cp cello.c cello.c.orig
    step3:
        change cello.c to:
        #include <stdio.h>
        int main(void) {
            printf("Hello World\n");
            return 0;
        }
    step4:
        diff -Naur cello.c.orig cello.c
        - means remove
        + means add
    step5:
        diff -Naur cello.c.orig cello.c > cello-output-first-patch.patch
    step6:
        cp cello.c.orig cello.c
    step7:
        patch < cello-output-first-patch.patch
    step8:
        make clean
    step9:
        make
    step10:
        ./cello
    done.    

3.Installing Arbitrary Artifacts
FHS: Filesystem Hierarchy Standard    
A big advantage of Linux and other Unix-like systems is the FHS.
Files installed from the RPM packages should be placed according to FHS.
For example, an executable file should go into a directory that is in the system PATH variable.

    3.1 using install to place Arbitrary artifacts in the system
        sudo install -m 0755 bello /usr/bin/bello
        Now bello is in a directory that is listed in the $PATH$ variable.
        Therefore, you can execute bello from any directory without specifying its full path:
        bello
    3.2 using make install 
        Add the install section to the makefile
        
        Makefile
        cello:
                gcc -g -o cello cello.c
        clean:
                rm cello
        install:
                mkdir -p $(DESTDIR)/usr/bin
                install -m 0755 cello $(DESTDIR)/usr/bin/cello
        The $(DESTDIR) variable is a GNU make built-in and is commonly used to specify installation to a directory different than the root directory.

4.Putting source code into tarball
    mkdir bellodir
    mv bello bello.orig bellodir
    tar -cvzf bellodir.tar.gz bellodir
    you will get bellodir.tar.gz
    bellodir.tar.gz     ->      bellodir.tar    ->  bellodir    ->  files
    
5.RPM
An RPM package is simply a file containing other files and information about them needed by the system. 
Specifically, 
an RPM package consists of the cpio archive, which contains the files, 
and the RPM header, which contains metadata about the package. 
The rpm package manager uses this metadata to determine dependencies, where to install files, and other information.
There are two types of RPM packages:
    source RPM (SRPM)
    binary RPM
SRPMs and binary RPMs share the file format and tooling, 
but have different contents and serve different purposes. 
An SRPM contains source code, optionally patches to it, 
and a SPEC file, which describes how to build the source code into a binary RPM. 
A binary RPM contains the binaries built from the sources and patches.


























