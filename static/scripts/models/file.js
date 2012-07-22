define(function (require, exports) {
  'use strict';

  var $           = require('jquery')
    , _           = require('underscore')
    , Backbone    = require('backbone')
    , utils       = require('utils');

  exports.File = Backbone.Model.extend({

    defaults: {
      selected: false
    , uploaded: false
    }

  , url: function () {
      var url = '/users/' + this.get('ownerId') + '/files';

      if (!this.isNew()) url += '/' + this.get('id');

      return url;
    }

  , initialize: function () {
      console.log('init file model');
    }

  , upload: function () {
      var file = this.get('raw')
        , that = this;

      var xhr = new XMLHttpRequest()
        , data = new FormData();
      data.append('file', file);
      data.append('name', this.get('name'));
      // _.each(this.attributes, function (value, attr) {
      //   console.log(attr);
      //   console.log(value);
      //   data.append(attr, value);
      // });
      console.log(data);

      xhr.file = file;
      xhr.upload.onprogress = function (e) {
        that.onProgress(e, that);
      }
      xhr.onreadystatechange = function (e) {
        that.onStateChange(e, that);
      };
      xhr.open('post', this.url(), true);
      xhr.send(data);
    }

    // Ajax file upload progress event
  , onProgress: function (e, context) {
      console.log(e);
    }

  , onStateChange: function (e, context) {
      console.log(e);

      context.set('uploaded', true);
    }

  });

});