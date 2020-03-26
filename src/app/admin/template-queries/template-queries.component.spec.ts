import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TemplateQueriesComponent } from './template-queries.component';

describe('TemplateQueriesComponent', () => {
  let component: TemplateQueriesComponent;
  let fixture: ComponentFixture<TemplateQueriesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TemplateQueriesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TemplateQueriesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
