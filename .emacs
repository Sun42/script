(require 'package)

;; Packages repo
;; (add-to-list 'package-archives '("marmalade" . "https://marmalade-repo.org/packages/"))
(add-to-list 'package-archives '("melpa" . "https://melpa.org/packages/"))
;; (add-to-list 'package-archives '("org" . "http://orgmode.org/elpa/") t) ; Org-mode's repository
(add-to-list 'package-archives '("elpy" . "http://jorgenschaefer.github.io/packages/"))
(package-initialize)
(when (not package-archive-contents)
  (package-refresh-contents))

(defvar myPackages
  '(better-defaults
    elpy
    tangotango-theme))

(mapc #'(lambda (package)
    (unless (package-installed-p package)
      (package-install package)))
      myPackages)

;; BASIC CUSTOMIZATION
;; --------------------------------------

(setq inhibit-startup-message t) ;; hide the startup message
(load-theme 'tangotango t) ;; load emacs theme
(global-linum-mode t) ;; enable line numbers globally

;; Parenthesis higlight
(show-paren-mode t)

;; Trailing whitespace
(setq-default show-trailing-whitespace t)

;; Show invisible chars
(setq whitespace-style '(space-mark))
(setq whitespace-display-mappings '((space-mark 32 [183] [46])))
(global-whitespace-mode 1)


;; Show column number
(setq column-number-mode t)

;; Elpy IDE
(elpy-enable)

;; Kivy Files
(add-to-list 'auto-mode-alist '("\\.kv\\'" . kivy-mode))


;; CUA Copy cut paste
(cua-mode t)
(setq cua-auto-tabify-rectangles nil) ;; Don't tabify after rectangle commands
(transient-mark-mode 1) ;; No region when it is not highlighted
    (setq cua-keep-region-after-copy t) ;; Standard Windows behaviour

;; Tell ansi-term to kill buffer after exit
(defadvice term-sentinel (around my-advice-term-sentinel (proc msg))
  (if (memq (process-status proc) '(signal exit))
      (let ((buffer (process-buffer proc)))
	ad-do-it
	(kill-buffer buffer))
    ad-do-it))
(ad-activate 'term-sentinel)

;; Tell ansi-term to use zsh by default
(defvar my-term-shell "/bin/zsh")
(defadvice ansi-term (before force-bash)
  (interactive (list my-term-shell)))
(ad-activate 'ansi-term)

(defadvice term (before force-bash)
  (interactive (list my-term-shell)))
(ad-activate 'term)

;; (defun shell ()
;;   (interactive)

;; Perso shortkeys
(global-set-key (kbd "C-c _") 'split-window-vertically)
(global-set-key (kbd "C-c i") 'split-window-horizontally)
(global-set-key (kbd "C-c k") 'kill-buffer-and-window)
(global-set-key (kbd "C-c j") 'kill-buffer)
(global-set-key (kbd "C-c o") 'other-window)
(global-set-key (kbd "C-x ;") 'comment-or-uncomment-region)
(global-set-key (kbd "C-d") 'kill-whole-line)
(global-set-key (kbd "C-e") 'elpy-multiedit-python-symbol-at-point)
(global-set-key (kbd "C-q") 'end-of-line)


;; Change background color
;;(require 'color-theme)
;;(color-theme-initialize)
;;(color-theme-install-frame-params
;;  '((background-color . "black")))


;; initial window settings
(setq initial-frame-alist
        '((background-color "#000000")))

;; subsequent window settings
;;(setq default-frame-alist
;;        (background-color . "honeydew")))
