export default class Macro {
  constructor(model) {
    this.age = model.age;
    this.weight = model.weight;
    this.gender = model.gender;
    this.height = model.height;
    this.activeLevel = Number(model.activeLevel);
    this.workActive = model.isWorkActive;
    this.program = model.goal;
    // set defaults and then change below if different Program
    this.carbsPercent = 0.45;
    this.protienPercent = 0.35;
    this.fatPercent = 0.30;
    this.programCorrection = 0;
    this.workFactor = 1;

    if (this.program === 'fat loss') {
      this.carbsPercent = 0.40;
      this.protienPercent = 0.30;
      // a positive number, the formula will subtrack it.
      this.programCorrection = 500;
    }

    if (this.workActive === 'active') {
      this.workFactor = 1.10;
    }

    this.BMR = 0;
    this.calories = 0;
    this.fat = 0;
    this.carbs = 0;
    this.protien = 0;
  }
  calculateBMR() {
    if (this.gender === 'female') {
      this.BMR = ((655 + (9.6 * this.weight)) + (1.8 * this.height)) - (4.7 * this.age);
    } else {
      this.BMR = 66 + (13.7 * this.weight) + (5 * this.height) - (6.8 * this.age);
    }
  }
  calculateCalories() {
    if (this.BMR === 0) {
      this.calculateBMR();
    }
    console.log('Active Level: ', this.activeLevel);
    console.log('Work Factor: ', this.workFactor);
    const c = (this.BMR * this.activeLevel);

    console.log('Total Cal ', c);

    console.log('Program Correction: ', this.programCorrection);

    this.calories = ((this.BMR * this.activeLevel) * this.workFactor) - this.programCorrection;
  }
  calculateMacros() {
    if (this.calories === 0) {
      this.calculateCalories();
    }
    const cal = this.calories;
    // the majgc numbers denote cal per gram.  Would be better to use constant
    // formula (total cal / Cal/g) * percent of diet.
    console.log('Sub Cal', cal);
    console.log('Fat percent', this.fatPercent);

    this.fat = Math.round((cal / 9) * this.fatPercent);
    this.carbs = Math.round((cal / 4) * this.carbsPercent);
    this.protien = Math.round((cal / 4) * this.protienPercent);
  }
  calculate() {
    this.calculateBMR();
    console.log('the BMR is: ', this.BMR);
    this.calculateCalories();
    this.calculateMacros();
  }
}

// To keep code clean, and not require the use of .default after the inport
// export const __useDefault = true;
