/**
 * Created by marcw on 2017-07-05.
 */


Vue.component('ibox', {

    template: '<div class="ibox"><div class="ibox-title"><slot name="title"></slot></div><div class="ibox-content"><slot name="content"></slot></div></div>'

});


new Vue({

    el: '#root'
});
