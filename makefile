include .env
include config.mk

# Default values
CONTEST_ID ?=
ATCODER_USERNAME ?=
ATCODER_PASSWORD ?=

# Docker image name
IMAGE_NAME = atcoder-env

.PHONY: build run clean help

build:
	@echo "Building Docker image..."
	docker build -t $(IMAGE_NAME) .

run:
	$(eval CONTEST_ID := $(if $(CONTEST_ID),$(CONTEST_ID),$(filter-out $@,$(MAKECMDGOALS))))
	@if [ -z "$(CONTEST_ID)" ]; then \
		echo "Error: CONTEST_ID is not set. Use 'make run CONTEST_ID=<id>' or 'make run <id>'"; \
		exit 1; \
	fi
	@echo "Running container for contest $(CONTEST_ID)..."
	docker run -it --rm \
		-v $(CURDIR):/atcoder \
		-v $(CURDIR)/core:/usr/local/lib/python3.11/site-packages/core \
		-e CONTEST_ID=$(CONTEST_ID) \
		-e LANGAGE=$(LANGAGE) \
		-e ATCODER_USERNAME=$(ATCODER_USERNAME) \
		-e ATCODER_PASSWORD=$(ATCODER_PASSWORD) \
		$(IMAGE_NAME)\
		bash

setup:
	@echo "Setting up AtCoder environment..."
	@echo "コンテナ内で実行する想定のコマンド"
	python3 /usr/local/bin/atcoder_helper.py setup --contest $(CONTEST_ID)

submit-%:
	@echo "Submitting solution to AtCoder..."
	@echo "コンテナ内で実行する想定のコマンド"
	oj submit https://atcoder.jp/contests/${CONTEST_ID}/tasks/${CONTEST_ID}_$* /workspaces/atcoder/contests/${CONTEST_ID}/$*/main.py -l 5055

ci:
	

clean:
	@echo "Removing Docker image..."
	docker rmi $(IMAGE_NAME)

help:
	@echo "Available commands:"
	@echo "  make build              - Build the Docker image"
	@echo "  make run CONTEST_ID=<id> - Run the Docker container with specified contest ID"
	@echo "  make clean              - Remove the Docker image"
	@echo "  make help               - Show this help message"
	@echo ""
	@echo "Environment variables:"
	@echo "  CONTEST_ID              - AtCoder contest ID (required for 'run')"
	@echo "  ATCODER_USERNAME        - AtCoder username for login"
	@echo "  ATCODER_PASSWORD        - AtCoder password for login"

# To handle arbitrary targets (like contest IDs)
%:
	@:

# Set default goal
.DEFAULT_GOAL := help