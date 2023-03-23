package logic

import (
	"fmt"
	"os"
	"os/exec"

	"github.com/go-git/go-git/v5"
	"github.com/maniizu3110/replace/logic/util"
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

func GitAddCommitPush(dir string) error {
	cmd := exec.Command("git", "add", ".")
	cmd.Dir = dir
	if output, err := cmd.CombinedOutput(); err != nil {
		return fmt.Errorf("git add error: %v, output: %s", err, string(output))
	}

	cmd = exec.Command("git", "commit", "-m", "auto commit")
	cmd.Dir = dir
	if output, err := cmd.CombinedOutput(); err != nil {
		return fmt.Errorf("git commit error: %v, output: %s", err, string(output))
	}

	cmd = exec.Command("git", "push")
	cmd.Dir = dir
	if output, err := cmd.CombinedOutput(); err != nil {
		return fmt.Errorf("git push error: %v, output: %s", err, string(output))
	}

	return nil
}
