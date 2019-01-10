	.global main

main:
	sub	sp, sp, #28
	movs	r3, #2
	str	r3, [sp, #12]
	movs	r3, #10
	str	r3, [sp, #16]
	movs	r3, #1
	str	r3, [sp, #4]
	movs	r3, #0
	str	r3, [sp, #8]
	b	.L2
.L3:
	ldr	r3, [sp, #4]
	ldr	r2, [sp, #12]
	mul	r3, r2, r3
	str	r3, [sp, #4]
	ldr	r3, [sp, #8]
	add	r3, r3, #1
	str	r3, [sp, #8]
.L2:
	ldr	r2, [sp, #8]
	ldr	r3, [sp, #16]
	cmp	r2, r3
	blt	.L3
	movs	r3, #1
	str	r3, [sp, #20]
	ldr	r2, [sp, #20]
	ldr	r3, [sp, #16]
	str r3, [sp, #24]
	mov r3, r2
	ldr r2, [sp, #24]
	lsl r3, r3, r2
	str	r3, [sp, #20]
	ldr	r2, [sp, #4]
	ldr	r3, [sp, #20]
	cmp	r2, r3
	bne	.L4
	movs	r3, #0
	b	.L5
.L4:
	mov r3, #255
.L5:
	mov	r0, r3
	add	sp, sp, #28
