@retirement
  Feature: Retirement Age Calculator
    As a social security user I want to calculate my retirement age.

    Scenario Outline: Input 1938 as year and September as month
      When the user enters a year value for "<year>" and a month value of "<month>"
      Then Then the output of "<age>" years and "<months>" months left to retirement will be shown

      Examples: Years and months
      | year | month | age | months |
      | 1915 | 10    | 65  | 0      |
      | 1938 | 9     | 65  | 2      |
      | 1950 | 8     | 66  | 0      |
      | 2019 | 3     | 67  | 0      |

    Scenario: Input 1950 as year and August as month
      When the user enters a year value for "1950" and a month value of "8"
      Then Then the output of "66" years and "0" months left to retirement will be shown

    Scenario: Input invalid format of year
      When the user enters an incorrect year value of "1800"
      Then The user gets asked to reenter valid input

    Scenario: Input invalid format of month
      When the user enters an incorrect month value of "14"
      Then The user gets asked to reenter valid input