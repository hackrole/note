Title: golang tips
Date: 2019-03-21
Category: programming
Tags: golang
Author: hackrole
Email: hack.role@gmail.com
Status: draft


# golang tips


## how to write golang

[offical how-to-write-go-code](https://golang.org/doc/code.html)

### all code in workspace, which different from other language


### import_path and package_name

1) import_path need to be unique

2) import_path is not package_name

3) for convenience, `import_path == vcs_base_url<github.com/user>/ + package_name``, but this is not neccesary

4) execute_program package name must be main

5) all file in same import path must have same package_name


## effective go

[effective go](https://golang.org/doc/effective_go.html#names)

### go examples

### format
gofmt auto do this.

use indentation instead of space

line length is at you wish.

### comment and doc

package_doc is before `package name`,
in many file package should only one-file define it.
it usually define in doc.go.

it should only be text, html is not good idea.


func/variable doc is comment immediately preceding a top-level declaration.
Every exported (capitalized) name in a program should have a doc comment.

### names

1) package name should be good: short, concise, evocative

2) packages are given lower case, single-word names; there should be no need for underscores or mixedCaps.

3) Getter -> <Owner>(Captial). setter -> (SetOwner)(with Set prefix)

4)  one-method interfaces are named by the method name plus an -er(Ex: Reader, Writer, Formatter)

5) Read/Write/String and so on not use in your func name. 

6) use MixCaps instead of underscore for multiword-names.

7) Semicolons is not required.

# control stucture

1) if/for support short declare

2) for is for/while/foreach

3) foreach => for i, v := range items

4) switch and fallthrough

5) type_switch
```golang
switch t := t.(type) {
    case bool: ...
    case int: ...
}
```


## the go programming spec

[offical go spec](https://golang.org/ref/spec)


# golang gc ISMM

[ISMM keynote about golang GC](https://blog.golang.org/ismmkeynote)

# golang for industrial programming

[golang for industrial programming](https://peter.bourgon.org/go-for-industrial-programming/)


1) flag better than environment-vars and config. environment-vars for secret-config

2) explicit dependencies

3) no package level variable

4) no func init

5) pkg structure around business-domain. 

6) never start a goroutine without know how it stop
