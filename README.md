<!--
Copyright 2020 Jonathan Haigh <jonathanhaigh@gmail.com>
SPDX-License-Identifier: MIT
-->
# `ju-jump` back end

[`ju-jump`][frontend] is a shell function that switches to a directory when
given an abbreviation for that directory as an argument. The abbreviations that
`ju-jump` understands are specified by the user.

The main element of the `ju-jump` back end is a Python 3 script that the `ju-jump` shell function uses to determine the path to a directory given an abbreviation.

The `ju-jump` back end also provides scripts to help with command line auto-completion and managing the set of abbreviations that `ju-jump` understands.

[frontend]: https://github.com/jonathanhaigh/ju-jump
