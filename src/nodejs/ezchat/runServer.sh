#!/bin/bash
node Server.js  2> ~/logs/ezchatStderr.txt < /dev/null &
disown
