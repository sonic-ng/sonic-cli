install:
	@mkdir -p /sonic-ng/cli
	install -c show config /sonic-ng/cli/
	_SHOW_COMPLETE=source show > show.sh && sudo mv show.sh /etc/bash_completion.d/show
	[ ! -e /usr/share/bash-completion/bash_completion ] && sudo install -c bash_completion /usr/share/bash-completion/bash_completion
	cp -af show_cli /sonic-ng/cli/
	cp -af config_cli /sonic-ng/cli/
