//Requirejs configuration to load the msa module
require.config({
  paths : {
    'msa' : '/nbextensions/msa_bundle'
  },
  shim : {
    msa : {
      exports : 'msa'
    }
  }
});

define(['jquery', 'underscore', 'jupyter-js-widgets', 'msa'],
function($, _, widgets, msa){
  console.log(msa);

  // create new instance of MSA
  var m = new msa.msa();

  var msaWidgetView = widgets.DOMWidgetView.extend({

    render : function(){
      msaWidgetView.__super__.render.apply(this, arguments);
      console.log("Rendering the MSA Widget");
      this.$el.append("<div id='msaDiv'>Displaying the sequence 3</div>");
      _.bindAll(this, "init_viewer");

      // Wait for the element to be added to the DOM
      this.displayed.then(this.init_viewer);
    },


    //Update the view whenever seqs is changed
    init_viewer : function(){
      console.log("Updating the view");

      //check if MSA object is created
      if (!m){

        var m = new msa.msa();
        m.el = document.getElementById('msaDiv');
        console.log(m);
      }

      var seqs = this.model.get('js_seqs');

      //Some listeners
      //this.listenTo(this.model, 'change:seqs', this.plot);

      this.listenTo(this.model, 'change:url', this.importUrl);

    },


    // Some functions

    plot : function(){
      console.log("Plotting the sequence");
      var msa_view = m.render();
      this.$el.append($(msa_view.el));
    },

    importUrl : function(){
      m.u.file.importURL(this.model.get('url'), function(err, model){
        console.log("Imported from URL");
      });
    }

  });

  return {
    msaWidgetView : msaWidgetView
  }
});
