Title: golang tools required
Date: 2019-03-19
Category: programming
Tags: golang,tools
Author: hackrole
Email: hack.role@gmail.com
Status: draft

# get from spacemacs or nvim

Last update: 2019-03-19

TODO

> 1) two level, not three.
>
> 2) move source-from to footer
>
> 3) add example usage or code example

## auto-completion

### gocode

code auto-completion, not recommand now

### lsp(go language server)

golang auto-completion tools speaks Language Server Protocol


#### gogetdoc

retrieve documention for item in go source code.
use to improve golang auto-completion


## source code linter

### golangci-lint

golang linters aggregator. 5 times faster thant gometalinter

### gometalinter

XXX DEPRECATED. use golangci-lint instead
tools to lint golang source code.
it can used to run many other lint tools concurrently

## source-code refactor

### godef

find symbol information in go source

### guru

tool for answering question about go source code.

### gorename

type-safe rename of identifiers in go source code

### goimports

update go import lines

### godoctor

golang source code refactoring tools

### gopkgs

list available go package that can be imported

## edit-helper tools

### fillstruct

fill a struct literal with default values.

### impl

generate methods stubs for implements an interface

### gotests(github.com/cweill/gotets/...)

make writing go tests easy. use to generate table driven tests based on its target source file
function.

[emacs tools to use gotests](https://github.com/s-kostyaev/go-gen-test)
package for generate tests for go code from emacs

### gomodifytags

tools to modify/update fields tags in structs

## unit test framework or tools

### gocheck

go testing framework build upon internal testing library

### goconvey
[goconvey](https://github.com/s-kostyaev/go-gen-test)


# TODO go-tools in youtube
