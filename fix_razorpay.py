#!/usr/bin/env python3
import os

os.chdir('d:\\shop\\E-commerce-Complete-Flutter-UI')

with open('lib/services/razorpay_service.dart', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find and fix the broken method
fixed_lines = []
i = 0
while i < len(lines):
    line = lines[i]
    
    # Look for the broken headers section
    if i < len(lines) - 1 and "'Content-Type': 'application/json'," in line and 'body:' in lines[i+1]:
        # Add the line with closing brace
        fixed_lines.append(line)
        i += 1
        # Fix the missing closing brace
        if 'body: jsonEncode' in lines[i]:
            fixed_lines.append("        },\n")
        fixed_lines.append(lines[i])
        i += 1
    # Fix the broken string literal in return statement
    elif "return data['success'] == true && data['verified" in line:
        fixed_lines.append("        return data['verified'] ?? false;\n")
        i += 2  # Skip the broken next line
    else:
        fixed_lines.append(line)
        i += 1

with open('lib/services/razorpay_service.dart', 'w', encoding='utf-8') as f:
    f.writelines(fixed_lines)

print("File fixed successfully")
