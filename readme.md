# HashConverter - Desec LAB.

## Contents:

<!--ts-->
   * [About](#about)
<!--te-->

About
============

During a pentesting we found a github with the code that the application used to generate the system hash. The code performs an md5 on the string, then a base64, then a sha1.

Find the password from the system generated hash:

806825f0827b628e81620f0d83922fb2c52c7136

Tip: use john's wordlist (password.lst)
Tip2: Create a script to read the wordlist and apply the algorithm above.


