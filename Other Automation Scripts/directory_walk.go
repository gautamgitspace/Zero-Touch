//list contents of a directory using GoLang
package main
import (
  "os"
  "fmt"
  "path/filepath"
)
func main() {
  root, _ := filepath.Abs(".")
  fmt.Println("PWD:",root)

  err := filepath.Walk(root, processPath)
  if err!=nil {
    panic(err)
  }
}

func processPath(path string, info os.FileInfo, err error) error {
  if err!=nil {
    return err
  }
  if path!="." {
    if info.IsDir() {
      fmt.Println("Directory:", path)
      }else{
        fmt.Println("File:", path)
      }
    }
    return nil
}
