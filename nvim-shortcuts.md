# Neovim Shortcuts Reference

## Navigation

### Window Navigation
                      | Shortcut   | Description        |
                      | ---------- | -------------      |
                      | `Ctrl+h`   | Move to left pane  |
                      | `Ctrl+j`   | Move to below pane |
                      | `Ctrl+k`   | Move to above pane |
                      | `Ctrl+l`   | Move to right pane |

### File Tree (nvim-tree)
                          | Shortcut    | Description               |
                          | ----------  | -------------             |
                          | `<leader>e` | Toggle file tree          |
                          | `<leader>f` | Find current file in tree |
                          | `a`         | Create new file (in tree) |
                          | `d`         | Delete file (in tree)     |
                          | `r`         | Rename file (in tree)     |
                          | `x`         | Cut file (in tree)        |
                          | `c`         | Copy file (in tree)       |
                          | `p`         | Paste file (in tree)      |
                          | `R`         | Refresh tree              |
                          | `q`         | Close tree                |

### Telescope (Fuzzy Finder)
                             | Shortcut                | Description       |
                             | ----------              | -------------     |
                             | `:Telescope find_files` | Find files        |
                             | `:Telescope live_grep`  | Search in files   |
                             | `:Telescope buffers`    | List open buffers |
                             | `:Telescope help_tags`  | Search help       |

---

## LSP (Language Server)

### Code Navigation
                    | Shortcut     | Description              |
                    | ----------   | -------------            |
                    | `gd`         | Go to definition         |
                    | `K`          | Show hover documentation |
                    | `<leader>ca` | Code action              |
                    | `<leader>rn` | Rename symbol            |
                    | `<leader>e`  | Show diagnostics         |

---

## Completion (nvim-cmp)

### Insert Mode Completion
                           | Shortcut     | Description                                                 |
                           | ----------   | -------------                                               |
                           | `Ctrl+Space` | Trigger completion                                          |
                           | `Enter`      | Confirm selection                                           |
                           | `Tab`        | Select next item / Jump to next snippet placeholder         |
                           | `Shift+Tab`  | Select previous item / Jump to previous snippet placeholder |
                           | `Ctrl+b`     | Scroll docs up                                              |
                           | `Ctrl+f`     | Scroll docs down                                            |
                           | `Ctrl+e`     | Abort completion                                            |

---

## Debugging (DAP)

### Debug Controls
                   | Shortcut     | Description                  |
                   | ----------   | -------------                |
                   | `F5`         | Continue / Start debugging   |
                   | `F10`        | Step over                    |
                   | `F11`        | Step into                    |
                   | `F12`        | Step out                     |
                   | `<leader>b`  | Toggle breakpoint            |
                   | `<leader>B`  | Set conditional breakpoint   |
                   | `<leader>dr` | Open debug REPL              |
                   | `<leader>dl` | Run last debug configuration |

---

## GitHub Copilot

### Copilot Suggestions
                        | Shortcut               | Description               |
                        | ----------             | -------------             |
                        | `Ctrl+J` (insert mode) | Accept Copilot suggestion |

### Copilot Chat
                 | Shortcut     | Description                     |
                 | ----------   | -------------                   |
                 | `<leader>cc` | Toggle Copilot Chat             |
                 | `<leader>ce` | Explain selection (visual mode) |
                 | `<leader>cr` | Review selection (visual mode)  |
                 | `<leader>cf` | Fix selection (visual mode)     |

---

## Basic Vim Motions

### Essential Movement
                       | Shortcut   | Description             |
                       | ---------- | -------------           |
                       | `h/j/k/l`  | Move left/down/up/right |
                       | `w`        | Jump to next word       |
                       | `b`        | Jump to previous word   |
                       | `0`        | Jump to start of line   |
                       | `$`        | Jump to end of line     |
                       | `gg`       | Jump to start of file   |
                       | `G`        | Jump to end of file     |
                       | `Ctrl+u`   | Scroll half page up     |
                       | `Ctrl+d`   | Scroll half page down   |

### Editing
            | Shortcut   | Description             |
            | ---------- | -------------           |
            | `i`        | Insert before cursor    |
            | `a`        | Insert after cursor     |
            | `I`        | Insert at start of line |
            | `A`        | Insert at end of line   |
            | `o`        | Insert new line below   |
            | `O`        | Insert new line above   |
            | `dd`       | Delete line             |
            | `yy`       | Yank (copy) line        |
            | `p`        | Paste after cursor      |
            | `P`        | Paste before cursor     |
            | `u`        | Undo                    |
            | `Ctrl+r`   | Redo                    |
            | `v`        | Visual mode (select)    |
            | `V`        | Visual line mode        |
            | `Ctrl+v`   | Visual block mode       |

### Search and Replace
                       | Shortcut         | Description               |
                       | ----------       | -------------             |
                       | `/pattern`       | Search forward            |
                       | `?pattern`       | Search backward           |
                       | `n`              | Next search result        |
                       | `N`              | Previous search result    |
                       | `:%s/old/new/g`  | Replace all occurrences   |
                       | `:%s/old/new/gc` | Replace with confirmation |

### File Operations
                    | Shortcut      | Description         |
                    | ----------    | -------------       |
                    | `:w`          | Save file           |
                    | `:q`          | Quit                |
                    | `:wq`         | Save and quit       |
                    | `:q!`         | Quit without saving |
                    | `:e filename` | Open file           |
                    | `:bn`         | Next buffer         |
                    | `:bp`         | Previous buffer     |
                    | `:bd`         | Close buffer        |

---

## Notes

- `<leader>` key is typically `\` or `Space` (check your config with `:echo mapleader`)
- LSP, Copilot, and DAP features only work for Python, Rust, C, and C++ files
- Many shortcuts work in specific modes: `n` = normal, `i` = insert, `v` = visual
