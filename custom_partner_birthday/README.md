# Partner Birthday Module

This Odoo module extends the partner functionality to include birthday tracking and automated reminders.

## Features

- Adds date of birth field to partners
- Calculates and displays the partner's age
- Automatically creates activities for salespersons to remind them about customer birthdays
- Includes a filter to easily find partners with birthdays set

## Installation

1. Copy this module to your Odoo addons directory
2. Update the modules list
3. Install the "Partner Birthday" module

## Usage

After installation, you'll see a new "Date of Birth" field in partner forms. When you set a date of birth for a partner:

1. The age field will be automatically calculated
2. A daily scheduled action will check for birthdays
3. When a partner has a birthday, the responsible salesperson will receive an activity reminding them to congratulate the partner

## Technical Details

- The module creates a daily scheduled action to check for birthdays
- For partners with birthdays on the current day, it creates activities for their assigned salesperson
- The age is calculated based on the date of birth and current date

## Dependencies

- base
- mail
- contacts
