package main

import (
	"fmt"

	"github.com/joho/godotenv"
	"github.com/maniizu3110/replace/logic"
	"github.com/maniizu3110/replace/logic/util.go"
)

func init() {
	err := godotenv.Load()
	if err != nil {
		panic(err)
	}
}

func main() {
	logic.Clone("https://github.com/maniizu3110/gittest.git", false)
	repoName, err := util.ExtractRepoName("https://github.com/maniizu3110/gittest.git")
	if err != nil {
		panic(err)
	}
	repoContent, err := logic.DirToStrings("./dist/" + repoName)
	if err != nil {
		panic(err)
	}
	message := "Change the output to include quotes from famous people.Also, please add one appropriate file that outputs the sad words"
	repoContent = append(repoContent, message)
	gptResponses, err := logic.CallGPT4(repoContent)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}
	for _, gptResponse := range gptResponses {
		pathContents, err := logic.ExtractPathsAndContents(gptResponse)
		if err != nil {
			fmt.Println("Error:", err)
			return
		}
		for _, pc := range pathContents {
			fmt.Println(pc.Path)
			logic.WiteFile(pc.Path, pc.Content)
		}
	}
}
