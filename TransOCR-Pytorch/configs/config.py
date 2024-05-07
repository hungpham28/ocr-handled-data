import yaml
from yaml.loader import SafeLoader
import os
from src.utils.utils import download_config

url_config = {
        'vgg_transformer':'vgg-transformer.yml',
        'resnet_transformer':'resnet_transformer.yml',
        'resnet_fpn_transformer':'resnet_fpn_transformer.yml',
        'vgg_seq2seq':'vgg-seq2seq.yml',
        'vgg_convseq2seq':'vgg_convseq2seq.yml',
        'vgg_decoderseq2seq':'vgg_decoderseq2seq.yml',
        'base':'/home/edabk/phumanhducanh/BKAI/TransOCR-Pytorch/configs/base.yml',
        }

class Cfg(dict):
    def __init__(self, config_dict):
        super(Cfg, self).__init__(**config_dict)
        self.__dict__ = self

    @staticmethod
    def load_config_from_file(fname):
        with open(url_config['base'], 'r') as f:
            base_config = yaml.load(f, Loader=SafeLoader)

        with open(fname, encoding='utf-8') as f:
            config = yaml.safe_load(f)

        base_config.update(config)
        return Cfg(base_config)
    
    @staticmethod
    def load_config_from_name(name):
        base_config = download_config(url_config['base'])
        # config = download_config(url_config[name])

        # base_config.update(config)
        #base_config = {}
        with open(os.path.join('/home/edabk/phumanhducanh/BKAI/TransOCR-Pytorch/configs',url_config[name]), encoding='utf-8') as f:
            config = yaml.safe_load(f)
        base_config.update(config)        
        return Cfg(base_config)

    def save(self, fname):
        with open(fname, 'w') as outfile:
            yaml.dump(dict(self), outfile, default_flow_style=False, allow_unicode=True)
