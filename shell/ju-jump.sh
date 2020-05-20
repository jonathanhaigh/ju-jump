#!/bin/sh

ju_jump() {
    JU_JUMP_PATH=$(ju-jump-backend "$@")
    JU_JUMP_RC=$?
    if [ "$JU_JUMP_RC" != 0 ]; then
        return "$JU_JUMP_RC"
    fi
    cd "$JU_JUMP_PATH"
}
