#!/usr/bin/env python
#

from __future__ import print_function
from random import randint
from socket import gethostname
from sys import exit, stderr
from commands import getoutput
from subprocess import call
from time import sleep
from os import environ

__author__ = "Rupe"
__date__ = "June 14 2015"
__copyright__ = "Linux Professional Training"
__version__ = "0.2"
__license__ = "GPL"
__email__ = "ruped24@gmail.com"


class Colors:
  Escape = "\033"
  Lred = "[91m"
  Lgre = "[92m"
  Lyel = "[93m"


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


class Tools:
  tool = {
    'helper': 'which',
    1: "setoolkit",
    2: "openvas-setup",
    3: "veil-evasion",
    4: "websploit"
  }


def who_did_it():
  print("        {0}".format("#" * 64))
  print("        {0}".format("Created by: %s." % __copyright__))
  print("        {0}".format("For training purposes only."))
  print("        {0}, {1}".format("Version %s" % __version__,
                                  "License %s" % __license__))
  print("        {0}".format("Written by: %s" % __author__))
  print("        {0}".format("#" * 64 + "\n\n"))


def main_menu():
  print("        {0}".format(
      c.Escape + c.Lyel +
      "1)  Set -- Social-Engineer Toolkit (SET), attacks against humans.\n"))
  print("        {0}".format(
      "2)  OpenVas --  Vulnerability scanning and vulnerability management.\n"))
  print("        {0}".format(
      "3)  Veil-Evasion -- Generate metasploit payloads bypass anti-virus.\n"))
  print("        {0}".format(
      "4)  Websploit -- WebSploit Advanced MITM Framework.\n"))
  print("        {0}".format(c.Escape + c.Lred + "5)  Exit Kill Chain\n"))


if __name__ == '__main__':
  try:
    raw_input
  except NameError:
    raw_input = input
  try:
    while True:
      stderr.write("\x1b[2J\x1b[H")
      call(['reset'])
      try:
        print(Header().headers[randint(1, 3)] + "\n\n")
        c = Colors()
        who_did_it()
        main_menu()
        try:
          tool = Tools().tool
          selected = int(
            raw_input(c.Escape + c.Lgre + gethostname() + "-gOtr00t"
                        ":> "))
          if selected < 1 or selected > 5:
            print("Select a number between 1 and 5")
            sleep(2)
          if selected is 5:
            exit(0)
          if selected is 1:
            call([getoutput(tool['helper'] + ' ' + tool[1])])
            sleep(1)
          if selected is 2:
            call([getoutput(tool['helper'] + ' ' + tool[2])])
            sleep(1)
          if selected is 3:
            call([getoutput(tool['helper'] + ' ' + tool[3])])
            sleep(1)
          if selected is 4:
            call([getoutput(tool['helper'] + ' ' + tool[4])])
            sleep(1)
        except ValueError:
          print("Select a number between 1 and 5")
          sleep(2)
      except SystemExit:
        exit(0)
  except OSError as err:
    print("\n [*] Check your path " + c.Escape + c.Lred + "%s\n %s" %
          (environ['PATH'], "[!] " + c.Escape + c.Lyel + "Can't find"),
          c.Escape + c.Lgre + tool[selected] + ", " + err[1],
          c.Escape + c.Lred + "Aborting!")
    sleep(2)
    pass
