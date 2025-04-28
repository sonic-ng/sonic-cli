build:
	@echo _SHOW_COMPLETE=source ./show > show.sh
	@echo _CONFIG_COMPLETE=source ./config > config.sh

install:
	@mkdir -p /sonic-ng/cli
	install -c show.sh /etc/bash_completion.d/show
	install -c config.sh /etc/bash_completion.d/config
	install -c show config /sonic-ng/cli/
	install -c bash_completion /usr/share/bash-completion/bash_completion
	cp -af show_cli /sonic-ng/cli/
	cp -af config_cli /sonic-ng/cli/
