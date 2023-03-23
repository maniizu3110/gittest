package logic

import (
	"fmt"
	"os"

	"github.com/go-git/go-git/v5"
	"github.com/maniizu3110/replace/logic/util.go"
)

const (
	distDir = "./dist/"
)

func Clone(repositoryUrl string, isPrivate bool) {
	repoName, err := util.ExtractRepoName(repositoryUrl)
	if err != nil {
		fmt.Printf("Error extracting repository name: %s\n", err)
		os.Exit(1)
	}

	_, err = git.PlainClone(distDir+repoName, false, &git.CloneOptions{
		URL:               repositoryUrl,
		RecurseSubmodules: git.DefaultSubmoduleRecursionDepth,
		Auth:              nil, // If the repository is private, you need to set up authentication here
	})

	if err != nil {
		fmt.Printf("Error cloning repository: %s\n", err)
		os.Exit(1)
	}

	fmt.Println("Repository cloned successfully")
}

func Add() {
	return
}

func Commit() {
	return
}

func Push() {
	return
}
