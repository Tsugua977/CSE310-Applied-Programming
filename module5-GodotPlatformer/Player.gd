extends KinematicBody2D

#Sets the velocity of the player to zero.
var velocity = Vector2.ZERO
#Sets up player max speed.
var playerMaxSpeed = 60
#Sets up the player's acceleration.
var playerAcceleration = 40
#Sets up the player's friction.
var playerFriction = 5
#Sets up the direction of the dash. the number one tells the program that the dash will happen on the x axis.
var dashDirection = Vector2(1, 0)
#Sets canDash to false.
var canDash = false
#Sets dashing to false.
var dashing = false
#Sets the dash force
var dashDistance = 200
#Sets fastFaliing to false.
var fastFalling = false
#Sets the jump force to -120.
var jumpHeight = -120
#Sets the jump release force to -40.
var jumpReleaseForce = -40
#Sets fastFalling to 35.
var fastFallingNum = 35
#Sets up the gravity.
var gravity = 5

#Updates the game to runs physics and movement of player.
func _physics_process(delta):
	#Sets dash function in _physics_process so it can be called at any time.
	dash()
	#Adds the gravity to the player's y velocity.
	velocity.y += gravity
	
	#The player input is set to zero.
	var input = Vector2.ZERO
	#If left or right are pressed, playerInput is changed to 1 or -1, respectively.
	input.x = Input.get_action_strength("ui_right") - Input.get_action_strength("ui_left")
	
	#If the playerInput is 0, this applies friction to them.
	if input.x == 0:
		apply_friction()
	#If the playerInput is not 0, this applies acceleration to them.
	else:
		apply_acceleration(input.x)
	
	#Checks if the player is touching the ground.
	if is_on_floor():
		#Sets fastFalling to false.
		fastFalling = false
		#If the player is touching the ground, jump height is added to their y velocity.
		if Input.is_action_just_pressed("ui_up"):
			velocity.y = jumpHeight
	else: 
		#If the input was just released, the y velocity is set to jumpReleaseFroce to drop the player down.
		if Input.is_action_just_released("ui_up") and velocity.y < jumpReleaseForce:
			velocity.y = jumpReleaseForce
		#If the player starts falling and is not dashing, they will fall faster.
		if velocity.y > 0 and not fastFalling and not dashing:
			#Adds the fastFallingNum to y velocity.
			velocity.y += fastFallingNum
			#Sets fast falling to true.
			fastFalling = true
	#Allows the player to move on screen.
	velocity = move_and_slide(velocity, Vector2.UP)

#Function to apply friction to the player.
func apply_friction():
	#Player's x velocity moves towards zero at the rate of playerFriction.
	velocity.x = move_toward(velocity.x, 0, playerFriction)

#Function to apply acceleration to player.
func apply_acceleration(direction):
	#Moves player towards the their max speed at the rate of playerAcceleration.
	velocity.x = move_toward(velocity.x, playerMaxSpeed * direction, playerAcceleration)
#Sets up the dash function.
func dash():
	#Recharges the dash if the player is on the floor.
	if is_on_floor():
		canDash = true
	#If the right arrow key is being pressed, than the dash direction is set to the right.
	if Input.is_action_pressed("ui_right"):
		dashDirection = Vector2(1, 0)
	#If the left arrow key is being pressed, than the dash direction is set to the left.
	if Input.is_action_pressed("ui_left"):
		dashDirection = Vector2(-1, 0)
	
	#If the dash button is pressed (Z) and canDash is true, then the player will dash.
	if Input.is_action_just_pressed("ui_dash") and canDash:
		velocity = dashDirection.normalized() * dashDistance
		#Doesn't allow the player to dash in mid-air again.
		canDash = false
		#Sets dashing to true.
		dashing = true
		#Creats a timer for how long the player can dash. Once the time runs out, dashing is set to false.
		yield(get_tree().create_timer(0.3), "timeout")
		#Dashing is set to false.
		dashing = false
