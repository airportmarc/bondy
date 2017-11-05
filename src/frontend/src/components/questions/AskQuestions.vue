<template>
  <b-card>
    <form-wizard
      color="#b0cd36"
      title=""
      subtitle=""
      @on-complete="onComplete"
    >
      <tab-content
        title="Contact Details"
        icon="glyphicon glyphicon-envelope"
        :before-change="validateTabOne">
        <!--Contact information.  Email address (too Soon?)-->
        <form>
          <vue-form-generator :schema="firstTabSchema" :model="model" :options="formOptions" ref="firstTabForm">

          </vue-form-generator>
        </form>
      </tab-content>

      <tab-content
        title="Personal details"
        icon="glyphicon glyphicon-user"
        :before-change="validateTabTwo">
        <form>
          <vue-form-generator :schema="secondTabSchema" :model="model" :options="formOptions" ref='secondTabForm'>

          </vue-form-generator>
        </form>
      </tab-content>

      <tab-content
        title="Fitness Levels"
        icon="glyphicon glyphicon-heart"
        :before-change="validateTabThree">
        <form>
          <vue-form-generator :schema="thirdTabSchema" :model="model" :options="formOptions" ref='thridTabForm'>

          </vue-form-generator>
        </form>
      </tab-content>

      <tab-content
        title="Dedication"
        icon="glyphicon glyphicon-plus"
        :before-change="validateTabFour">
        <form>
          <vue-form-generator :schema="fourthTabSchema" :model="model" :options="formOptions" ref='fourthTabForm'>

          </vue-form-generator>
        </form>
      </tab-content>
    </form-wizard>
  </b-card>
</template>

<script>
  import axios from 'axios';
  import Cookie from 'js-cookie';

  const crsf = Cookie.get('csrftoken');

  axios.defaults.headers.common['X-CSRFToken'] = crsf;

  // const Macro = require('../utls/calculations').default;

  export default {
    data() {
      return {
        model: {
          id: 1,
          email: '',
          firstName: '',
          lastName: '',
          age: '',
          gender: '',
          weight: '',
          height: '',
          activeLevel: '',
          goal: '',
          isWorkActive: '',
          howReady: '',
          howImportant: '',
          password: 'J0hnD03!x4',
          fat: '',
          protein: '',
          carbs: '',
          calories: '',
        },
        firstTabSchema: {
          groups: [
            {
              legend: 'Contact Details',
              fields: [
                {
                  type: 'input',
                  inputType: 'text',
                  label: 'First Name',
                  model: 'firstName',
                  id: 'user_firstName',
                  placeholder: 'First Name',
                  validator: ['string', 'required'],
                },
                {
                  type: 'input',
                  inputType: 'text',
                  label: 'Last Name',
                  model: 'lastName',
                  id: 'user_lastName',
                  placeholder: 'Last name',
                  validator: ['string', 'required'],
                },
                {
                  type: 'input',
                  inputType: 'text',
                  label: 'Email',
                  model: 'email',
                  placeholder: 'Email',
                  validator: ['email', 'required'],
                },
              ],
            },
          ],
        },
        secondTabSchema: {
          fields: [
            {
              type: 'input',
              inputType: 'number',
              label: 'Age',
              model: 'age',
              styleClasses: 'col-md-6',
              id: 'user_age',
              placeholder: 'Age',
              validator: ['number', 'required'],
            },
            {
              type: 'select',
              label: 'Gender',
              model: 'gender',
              id: 'user_gender',
              placeholder: 'Gender',
              styleClasses: 'col-md-6',
              values: ['Male', 'Female'],
            },
            {
              type: 'input',
              inputType: 'number',
              label: 'Height (cm)',
              model: 'height',
              id: 'user_height',
              styleClasses: 'col-md-6',
              placeholder: 'Height',
              validator: ['number', 'required'],
            },
            {
              type: 'input',
              inputType: 'number',
              label: 'Weight (Kg)',
              model: 'weight',
              id: 'user_weight',
              styleClasses: 'col-md-6',
              placeholder: 'Weight',
              validator: ['number', 'required'],
            },
          ],
        },
        thirdTabSchema: {
          fields: [
            {
              type: 'select',
              label: 'How Active of a Person are you currently?',
              selectOptions: {
                hideNoneSelectedText: true
              },
              model: 'activeLevel',
              id: 'user_activeLevel',
              values() {
                return [
                  { id: '1.2', name: 'Im quite sedentary and dont move around a lot.' },
                  { id: '1.375', name: 'I workout 1-2 times a week' },
                  { id: '1.55', name: 'I workout 3-4 times a week' },
                  { id: '1.725', name: 'I workout 5-7 times a week' },
                ];
              },
            },
            {
              type: 'select',
              label: 'Does your job require you to be active?',
              selectOptions: {
                hideNoneSelectedText: true
              },
              model: 'isWorkActive',
              id: 'user_activeLevel',
              values() {
                return [
                { id: '0', name: 'No, not at all' },
                { id: '1', name: 'Yep, im quite active an on my feet throughout the day' }
                ];
              }
            },
            {
              type: 'select',
              label: 'What is your goal?',
              model: 'goal',
              id: 'user_goal',
              selectOptions: {
                hideNoneSelectedText: true
              },
              values() {
                return [
                { id: '0', name: 'To lose weight, mostly fat' },
                { id: '1', name: 'To maintain my current weight but make some changes to my body' },
                { id: '2', name: 'To gain some weight and add more muscle to my composition' },
                ];
              }
            },
          ],
        },
        fourthTabSchema: {
          fields: [
            {
              type: 'select',
              label: 'How important is it to you to make lifestyle changes (modify what you are currently doing) to support your health and wellness?',
              model: 'howReady',
              id: 'user_activeLevel',
              selectOptions: {
                hideNoneSelectedText: true
              },
              values: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
            },
            {
              type: 'select',
              label: 'How CONFIDENT are you in your own abilities to make lifestyle changes to support your health and wellness?',
              model: 'howImportant',
              id: 'user_howImportant',
              selectOptions: {
                hideNoneSelectedText: true
              },
              values: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
            },

          ],
        },
        formOptions: {
          validationErrorClass: 'has-error',
          validationSuccessClass: 'has-success',
          validateAfterChanged: true
        },
      };
    },
    methods: {
      validateTabOne: function validateTabOne() {
        if (!this.$refs.firstTabForm.validate()) {
          return false;
        }

        return axios.get('/api/initalEmail', {
          params: {
            email_address: this.model.email,
            status: 'subscribed',
            fname: this.model.firstName,
            lname: this.model.lastName,
          },
        })
          .then((response) => {
            if(response.data.local.pk){
              this.model.id = pk
            }
            return true;
          })
          .catch((error) => {
            return false;
          });
      },
      validateTabTwo: function validateTabTwo() {
        console.log(this.$refs.secondTabForm.validate());
        if (!this.$refs.secondTabForm.validate()) {
          return false;
        }
        return true;
      },
      validateTabThree: function validateTabThree() {
        if (!this.$refs.thridTabForm.validate()) {
          return false;
        }
        return true;
      },
      validateTabFour: function validateTabFour() {
        if (!this.$refs.fourthTabForm.validate()) {
          return false;
        }
        return true;
      },
      onComplete: function onComplete() {
        const payload = JSON.stringify(this.model);
        const xhr = new XMLHttpRequest();
        xhr.open('POST', '/api/initalFormComplete', true);
        xhr.onreadystatechange = function onreadystatechange() {
          if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);
            window.location.href = '/questions/complete/' + response.id;
          }
        };
        xhr.setRequestHeader('X-CSRFToken', crsf);
        xhr.send(payload);
        // return axios.post('', {
        //   params: {
        //     model: payload
        //   },
        // })
        // .then(() => {
        //   return true;
        // })
        // .catch((error) => {
        //   console.log(error);
        //   return false;
        // });
      },
    },
  };

</script>

<style>

</style>
