 
Hex to RGBA Function Documentation
Function Overview
The hex_to_rgba function converts hexadecimal color strings into RGBA (Red, Green, Blue, Alpha) color values. It handles multiple hex color formats including those with and without transparency.
Parameters
•	hex_color: A string representing a color in hexadecimal format. Can include the leading '#' character.
Return Value
A tuple of four integers (r, g, b, alpha) where:
•	r: Red component (0-255)
•	g: Green component (0-255)
•	b: Blue component (0-255)
•	alpha: Transparency component (0-255), where 0 is fully transparent and 255 is fully opaque
Function Breakdown
Step 1: Normalize Input
if hex_color.startswith("#"):
    hex_color = hex_color[1:]
•	Removes the leading '#' character if present
•	This allows the function to accept both formats: "#abc" and "abc"
Step 2: Validate Input
if not is_hexadecimal(hex_color):
    raise Exception("not a hex color string")
•	Checks if the string contains only valid hexadecimal characters (0-9, A-F)
•	Raises an exception if the input is not a valid hex string
Step 3: Determine Format and Prepare Values
hex_length = len(hex_color)
•	Gets the length of the hex string to determine its format
The function then handles four standard formats:
3-Digit Format (#RGB)
if hex_length == 3:
    hex_color = ''.join(c * 2 for c in hex_color)
•	Expands each digit by doubling it: "abc" becomes "aabbcc"
•	This converts shorthand notation to the full 6-digit format
•	Example: "abc" → "aabbcc" (equivalent to "aabbcc")
4-Digit Format (#RGBA)
elif hex_length == 4:
    r, g, b, a = hex


