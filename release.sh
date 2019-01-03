#!/usr/bin/env bash

set -x

# create release
CALVER=$(date +%Y%m%d%H%M%S)
hub release create -m "$CALVER" $CALVER
