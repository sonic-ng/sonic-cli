_show_completion() {
    local IFS=$'\t'
    COMPREPLY=( $( env COMP_WORDS="${COMP_WORDS[*]}" \
                   COMP_CWORD=$COMP_CWORD \
                   _SHOW_COMPLETE=complete-bash $1 ) )
    return 0
}

complete -F _show_completion -o default show
