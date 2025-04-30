_config_completion() {
    local IFS=$'\t'
    COMPREPLY=( $( env COMP_WORDS="${COMP_WORDS[*]}" \
                   COMP_CWORD=$COMP_CWORD \
                   _CONFIG_COMPLETE=complete-bash $1 ) )
    return 0
}

complete -F _config_completion -o default config
