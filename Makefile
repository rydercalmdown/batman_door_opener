PI_IP_ADDRESS=10.0.0.89
PI_USERNAME=pi

.PHONY: copy
copy:
	@rsync -a $(shell pwd) --exclude env $(PI_USERNAME)@$(PI_IP_ADDRESS):/home/$(PI_USERNAME) 

.PHONY: shell
shell:
	@ssh $(PI_USERNAME)@$(PI_IP_ADDRESS)

.PHONY: install
install:
	@cd deployment && bash install.sh

.PHONY: install-raspberry-pi
install-raspberry-pi:
	@cd deployment && bash install_raspberry_pi.sh
	@make install

.PHONY: run
run:
	@. env/bin/activate && cd src && python app.py
