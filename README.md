# Flight Booking

[![Build Status](https://travis-ci.org/ascii-dev/flight-booking.svg?branch=develop)](https://travis-ci.org/ascii-dev/flight-booking)
[![Maintainability](https://api.codeclimate.com/v1/badges/ce2535ff7a8508bbb623/maintainability)](https://codeclimate.com/github/ascii-dev/flight-booking/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/ce2535ff7a8508bbb623/test_coverage)](https://codeclimate.com/github/ascii-dev/flight-booking/test_coverage)
[![Reviewed by Hound](https://img.shields.io/badge/Reviewed_by-Hound-8E64B0.svg)](https://houndci.com)
[![Author: Samuel Afolaranmi](https://img.shields.io/badge/Author-Samuel%20Afolaranmi-orange.svg)](https://twitter.com/asciidev)

Flight booking is a flight booking application what allows a company offer flight booking and 
ticketing services to their customers.

An admin can add airplane and flight schedules for each airplane while a customer can go online
to book each flight schedule that fits in to their travel plan.

### Features
> - Both admins and users can login
> - A user can create an account
> - Users can upload passport photographs
> - Users can book flight tickets
> - Admins can add airplanes
> - Admins can add flight schedules
> - Users can check the status of their flights
 
 ### How to setup
 ##### Requirements
 In  order to setup this project locally, you need to have the following software requirements
 set up:
 > - PostgreSQL
 > - Python (*version 3.7*)
 > - Git
 > - Pipenv
 
 ##### Steps to setup
 > - Pull in the project: `git clone https://github.com/ascii-dev/flight-booking.git`
 > - Step into the project's directory: `cd flight-booking`
 > - Create virtual environment: `pipenv shell`
 > - Create the databases: `flight_booking` & `flight_booking_test`
 > - Copy `.env.sample` to `.env`: `cp .env.sample .env` and fill it out
 > - Start the server with `flask run`
 
 ### Project Links
 > PivotalTracker Board: `https://www.pivotaltracker.com/n/projects/2350555`
 
 ### Author
 [Samuel Afolaranmi](https://twitter.com/asciidev)
 