#!/usr/bin/env python
#

from __future__ import print_function
from random import randint
from socket import gethostname
from sys import exit, stdout, stderr
from commands import getoutput
from subprocess import call
from time import sleep
from os import environ, devnull
from os.path import isfile, basename

fnull = open(devnull, 'w')

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
      3: "setoolkit",
      4: "openvas-setup",
      5: "veil-evasion",
      6: "websploit",
      7: "msfconsole",
      8: "wifite"
  }


class TorIptables(object):
  def __init__(self):
    self.virtual_net = "10.0.0.0/10"
    self.non_tor_net = ["192.168.0.0/16", "172.16.0.0/12"]
    self.non_tor = ["127.0.0.0/9", "127.128.0.0/10", "127.0.0.0/8"]
    self.tor_uid = getoutput("id -ur debian-tor")  # Tor user uid
    self.trans_port = "9040"  # Tor port
    self.tor_config_file = '/etc/tor/torrc'
    self.torrc = '''
## Inserted by %s for tor iptables rules set
## Transparently route all traffic thru tor on port %s
VirtualAddrNetwork %s
AutomapHostsOnResolve 1
TransPort %s
DNSPort 53
''' % (basename(__file__), self.trans_port, self.virtual_net, self.trans_port)

  def flush_iptables_rules(self):
    call(["iptables", "-F"])
    call(["iptables", "-t", "nat", "-F"])

  def load_iptables_rules(self):
    self.flush_iptables_rules()
    if self.non_tor_net[0] not in self.non_tor:
      self.non_tor.extend(self.non_tor_net)

    call(["iptables", "-t", "nat", "-A", "OUTPUT", "-m", "owner", "--uid-owner",
          "%s" % self.tor_uid, "-j", "RETURN"])
    call(["iptables", "-t", "nat", "-A", "OUTPUT", "-p", "udp", "--dport", "53",
          "-j", "REDIRECT", "--to-ports", "53"])

    for net in self.non_tor:
      call(["iptables", "-t", "nat", "-A", "OUTPUT", "-d", "%s" % net, "-j",
            "RETURN"])

    call(["iptables", "-t", "nat", "-A", "OUTPUT", "-p", "tcp", "--syn", "-j",
          "REDIRECT", "--to-ports", "%s" % self.trans_port])

    call(["iptables", "-A", "OUTPUT", "-m", "state", "--state",
          "ESTABLISHED,RELATED", "-j", "ACCEPT"])

    for net in self.non_tor:
      call(["iptables", "-A", "OUTPUT", "-d", "%s" % net, "-j", "ACCEPT"])

    call(["iptables", "-A", "OUTPUT", "-m", "owner", "--uid-owner", "%s" %
          self.tor_uid, "-j", "ACCEPT"])
    call(["iptables", "-A", "OUTPUT", "-j", "REJECT"])

    # Restart Tor
    call(["service", "tor", "restart"], stdout=fnull, stderr=fnull)


def who_did_it():
  print("        {0}".format("#" * 64))
  print("        {0}".format("Created by: %s." % __copyright__))
  print("        {0}".format("For training purposes only."))
  print("        {0}, {1}".format("Version %s" % __version__, "License %s" %
                                                 __license__))
  print("        {0}".format("Written by: %s" % __author__))
  print("        {0}".format("#" * 64 + "\n\n"))


def main_menu():
  print("        {0}".format(
      c.Escape + c.Lyel +
      "1)  Anonymizer -- Load Tor Iptables rules, route all traffic thru Tor.\n"))
  print("        {0}".format(
      "2)  De-Anonymizer -- Flush Tor Iptables rules set to default rules.\n"))
  print("        {0}".format(
      "3)  Set -- Social-Engineer Toolkit (SET), attacks against humans.\n"))
  print("        {0}".format(
      "4)  OpenVas --  Vulnerability scanning and vulnerability management.\n"))
  print("        {0}".format(
      "5)  Veil-Evasion -- Generate metasploit payloads bypass anti-virus.\n"))
  print("        {0}".format(
      "6)  Websploit Framework -- WebSploit Advanced MITM Framework.\n"))
  print("        {0}".format(
      "7)  Metasploit Framework -- Executing exploit code against target.\n"))
  print("        {0}".format(
      "8)  WiFite -- Automated wireless auditor, designed for Linux.\n"))
  print("        {0}".format(c.Escape + c.Lred + "9)  Exit Kill Chain\n"))


def anon_status():
  anon = getoutput("iptables -S -t nat | grep 53")
  if anon:
    print("        {0} {1}".format("Anonymizer status",
                                   c.Escape + c.Lgre + "[ON]\n"))
  else:
    print("        {0} {1}".format("Anonymizer status",
                                   c.Escape + c.Lred + "[OFF]\n"))


if __name__ == '__main__':
  load_tables = TorIptables()
  try:
    raw_input
  except NameError:
    raw_input = input
  try:
    while True:
      stderr.write("\x1b[2J\x1b[H")
      call(['reset'])
      try:
        c = Colors()
        print(c.Escape + "[" + repr(randint(92, 97)) + "m" +
              Header().headers[randint(1, 3)] + "\n\n")
        who_did_it()
        anon_status()
        main_menu()
        try:
          tool = Tools().tool
          selected = int(
              raw_input(c.Escape + c.Lgre + gethostname() + "-gOtr00t"
                        ":> "))
          if selected < 1 or selected > 9:
            print("Select a number between 1 and 9")
            sleep(2)
          if selected is 9:
            exit(0)
          if selected is 1:
            if isfile(load_tables.tor_config_file):
              if not 'VirtualAddrNetwork' in open(
                  load_tables.tor_config_file).read():
                with open(load_tables.tor_config_file, 'a+') as torrconf:
                  torrconf.write(load_tables.torrc)
            load_tables.load_iptables_rules()
          sleep(1)

          if selected is 2:
            load_tables.flush_iptables_rules()
            sleep(1)
          if selected is 3:
            call(['clear'])
            call([getoutput(tool['helper'] + ' ' + tool[3])])
            sleep(1)
          if selected is 4:
            call(['clear'])
            call([getoutput(tool['helper'] + ' ' + tool[4])])
            sleep(1)
          if selected is 5:
            call(['clear'])
            call([getoutput(tool['helper'] + ' ' + tool[5])])
            sleep(1)
          if selected is 6:
            call(['clear'])
            call([getoutput(tool['helper'] + ' ' + tool[6])])
            sleep(1)
          if selected is 7:
            call(['clear'])
            call([getoutput(tool['helper'] + ' ' + tool[7])])
            sleep(1)
          if selected is 8:
            call(['clear'])
            call([getoutput(tool['helper'] + ' ' + tool[8])])
            sleep(5)
        except ValueError:
          print("Select a number between 1 and 9")
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
