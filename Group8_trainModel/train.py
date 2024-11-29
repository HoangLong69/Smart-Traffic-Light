if __name__ == '__main__':
    import torch
    from ultralytics import YOLO

    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    model = YOLO('yolov5n6u.pt')

    results = model.train(data='custom_dataset.yaml', epochs=50, device=device, batch=32)
