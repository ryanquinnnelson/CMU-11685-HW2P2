import logging

import octopus.models.resnets as resnets


class ResnetHandler:
    def __init__(self, model_type, in_features, num_classes):
        logging.info('Initializing model handling...')
        self.model_type = model_type
        self.in_features = in_features
        self.num_classes = num_classes

    def get_model(self):
        logging.info('Initializing model...')
        model = None

        if self.model_type == 'Resnet18':
            model = resnets.Resnet18(self.in_features, self.num_classes)

            # check if resnet18 matches official version
            # from torchsummary import summary
            # print(summary(model, (3, 224, 224)))
            # import torchvision.models as md
            # print(summary(md.resnet18(False), (3, 224, 224)))

        if self.model_type == 'Resnet34':
            model = resnets.Resnet34(self.in_features, self.num_classes)

            # check if resnet34 matches official version
            # from torchsummary import summary
            # print(summary(model, (3, 224, 224)))
            # print()
            # import torchvision.models as md
            # print(summary(md.resnet34(False), (3, 224, 224)))

        logging.info(f'Model initialized:\n{model}')
        return model