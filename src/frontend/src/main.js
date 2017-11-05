// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import BootstrapVue from 'bootstrap-vue';
import VueFormWizard from 'vue-form-wizard';
import VueFormGenerator from 'vue-form-generator';
import 'vue-form-wizard/dist/vue-form-wizard.min.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import 'bootstrap/dist/css/bootstrap.css';
import askquestions from './components/questions/AskQuestions';
import feildIconBox from './components/feilds/feildIconBox';

Vue.component('feildIconBox', feildIconBox);
require('../../static/css/project.css');
require('../../static/css/style.css');
require('nouislider');


Vue.use(VueFormGenerator);
Vue.use(BootstrapVue);
Vue.use(VueFormWizard);


Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  components: {
    askquestions,
  },
});
