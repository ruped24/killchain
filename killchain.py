#!/usr/bin/env python
#

from __future__ import print_function
from random import randint
from socket import gethostname
from sys import exit, stderr
from subprocess import call
from time import sleep

__author__ = "Rupe"
__date__ = "June 14 2015"
__copyright__ = "Linux Professional Training"
__version__ = "0.1"
__license__ = "GPL"
__email__ = "ruped24@gmail.com"

Escape = "\033"
Lred = "[91m"
Lgre = "[92m"
Lyel = "[93m"


def who_did_it():
    print("        {}".format("#" * 64))
    print("        {}".format("Created by: %s." % __copyright__))
    print("        {}".format("For training purposes only."))
    print("        {}".format("Version %s, License %s" %
                              (__version__, __license__)))
    print("        {}".format("Written by: %s" % __author__))
    print("        {}".format("#" * 64 + "\n\n"))


tools = {
    1: "setoolkit",
    2: "openvas-setup",
    3: "Veil-Evasion.py",
    4: "websploit"
}


def main_menu():
    print("        {}".format(
        Escape + Lyel +
        "1)  Set -- Social-Engineer Toolkit (SET), attacks against humans.\n"))
    print("        {}".format(
        "2)  OpenVas --  Vulnerability scanning and vulnerability management.\n"))
    print("        {}".format(
        "3)  Veil-Evasion -- Generate metasploit payloads bypass anti-virus.\n"))
    print("        {}".format(
        "4)  Websploit -- WebSploit Advanced MITM Framework.\n"))
    print("        {}".format(Escape + Lred + "5)  Exit Kill Chain\n"))


class Header:
        headers = {
            1: r"""
         **   ** **  **  **         ******  **                **
        /**  ** //  /** /**        **////**/**               //
        /** **   ** /** /**       **    // /**       ******   ** *******
        /****   /** /** /**      /**       /******  //////** /**//**///**
        /**/**  /** /** /**      /**       /**///**  ******* /** /**  /**
        /**//** /** /** /**      //**    **/**  /** **////** /** /**  /**
        /** //**/** *** ***       //****** /**  /**//********/** ***  /**
        //   // // /// ///         //////  //   //  //////// // ///   //   """,
            2: r"""
        KK  KK iii lll lll     CCCCC  hh              iii
        KK KK      lll lll    CC    C hh        aa aa     nn nnn
        KKKK   iii lll lll    CC      hhhhhh   aa aaa iii nnn  nn
        KK KK  iii lll lll    CC    C hh   hh aa  aaa iii nn   nn
        KK  KK iii lll lll     CCCCC  hh   hh  aaa aa iii nn   nn  """,
            3: r"""
        $$\   $$\ $$\ $$\ $$\        $$$$$$\  $$\                 $$\
        $$ | $$  |\__|$$ |$$ |      $$  __$$\ $$ |                \__|
        $$ |$$  / $$\ $$ |$$ |      $$ /  \__|$$$$$$$\   $$$$$$\  $$\ $$$$$$$\
        $$$$$  /  $$ |$$ |$$ |      $$ |      $$  __$$\  \____$$\ $$ |$$  __$$\
        $$  $$<   $$ |$$ |$$ |      $$ |      $$ |  $$ | $$$$$$$ |$$ |$$ |  $$ |
        $$ |\$$\  $$ |$$ |$$ |      $$ |  $$\ $$ |  $$ |$$  __$$ |$$ |$$ |  $$ |
        $$ | \$$\ $$ |$$ |$$ |      \$$$$$$  |$$ |  $$ |\$$$$$$$ |$$ |$$ |  $$ |
        \__|  \__|\__|\__|\__|       \______/ \__|  \__| \_______|\__|\__|  \__|  """,
        }


if __name__ == '__main__':
    try:
        while True:
            stderr.write("\x1b[2J\x1b[H")
            call(['reset'])
            try:
                print(Header().headers[randint(1, 3)] + "\n\n")
                who_did_it()
                main_menu()
                try:
                    selected = int(
                        raw_input(Escape + Lgre + gethostname() + "-gOtr00t"
                                  ":> "))
                    if selected < 1 or selected > 5:
                        print("Select a number between 1 and 5")
                        sleep(2)
                    if selected == 5:
                        exit(0)
                    if selected == 1:
                        call([tools[1]])
                        sleep(1)
                    if selected == 2:
                        call([tools[2]])
                        sleep(1)
                    if selected == 3:
                        call([tools[3]])
                        sleep(1)
                    if selected == 4:
                        call([tools[4]])
                        sleep(1)
                except ValueError:
                    print("Select a number between 1 and 5")
                    sleep(2)
            except SystemExit:
                exit(0)
    except Exception as err:
        print("\nCheck your path, %s.\n" % err)
        sleep(2)
        pass