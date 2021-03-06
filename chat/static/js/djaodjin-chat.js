(function ($) {
    "use strict";


    function DjChat(el, options){
        this.$root = $(el);
        this.options = options;
        this.init();

    }

    DjChat.prototype = {
        init: function(){
            var self = this;

            self.$chatSend = self.findPrefixed('chatsend');
            self.$chatInput = self.findPrefixed('chatinput');
            self.$chatLog = self.findPrefixed('chatlog');

            self.chatApi = new ChatApi();
            self.chatApi.on('connect', function(){
                self.chatApi.subscribe();
                self.chatApi.get_messages()
            });


            self.chatApi.on('message_from', function(message){
                var $message = $('<div/>');
                $message.addClass(self.options.cssPrefix + 'chatmessage')
                $message.text(message.from + ': ' + message.text);

                self.$chatLog.append($message);
            });
            self.chatApi.on('message', function(message){
                var $message = $('<div/>');
                $message.addClass(self.options.cssPrefix + 'chatmessage')
                $message.text('me: ' + message);

                self.$chatLog.append($message);
            });
            self.chatApi.on('get_messages_reply', function(reply){
                var messages = reply['messages'];
                for (var i = messages.length-1; i >= 0; i --){
                    var message = messages[i];

                    var $message = $('<div/>');
                    $message.text((message.from || 'me') + ': '+  message.text);
                    self.$chatLog.append($message);
                }
            })



            self.$chatSend.on('click', self.processMessageSubmit);
            self.$chatInput.on('keydown', function (event){
                if (event.which == 13 || event.keyCode == 13) {
                    event.preventDefault();
                    self.processMessageSubmit();
                    return false;
                }
                return true;
            });

        },
        processMessageSubmit: function(){
            var self = this;
            var message = self.$chatInput.val();

            self.chatApi.send(message)
            self.$chatInput.val('');
        },
        findPrefixed: function(name){

            var selector = '.' + this.options.cssPrefix + name;
            return this.$root.find(selector);
        }
    }

    $.fn.djchat = function(options) {
        var opts = $.extend( {}, $.fn.djchat.defaults, options );
        return new DjChat($(this), opts);
    };

    $.fn.djchat.defaults = {
        cssPrefix: 'djaodjin-chat-',
    };
})(jQuery);
