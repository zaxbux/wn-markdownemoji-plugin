<?php namespace Zaxbux\MarkdownEmoji;

use Event;
use System\Classes\PluginBase;
use Zaxbux\MarkdownEmoji\Classes\EmojiLibrary;

class Plugin extends PluginBase
{
    public function boot() {
			Event::listen('markdown.parse', function($text, $data) {
				$data->text = EmojiLibrary::replaceShortcodes($data->text);
			});
		}
}
